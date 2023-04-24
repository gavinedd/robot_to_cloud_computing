from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse, HttpResponseForbidden
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import check_password
from django.utils.timezone import now
from django.conf import settings
from datetime import datetime, date, timedelta

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

import json
import uuid

from ..models import FrontendUser


class UserLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            user = FrontendUser.objects.get(email=request.data.get('email'))

            if user is not None and check_password(request.data.get('password'), user.password) and user.is_active:
                token = RefreshToken.for_user(user)

                response = dict(
                    refresh=str(token),
                    access=str(token.access_token),
                )

                user.last_login = now()
                user.save()

                return JsonResponse(response)
            else:
                raise PermissionError("User does not exist or is not active")
        except (FrontendUser.DoesNotExist, PermissionError):
            return HttpResponse("Invalid email/password pair", status=401)
        except (json.JSONDecodeError, IntegrityError, TypeError, KeyError, ValueError):
            return HttpResponseBadRequest("Invalid request")


class GetPublicKey(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        public_key = settings.PUBLIC_TOKEN_VERIFYING_KEY

        response = dict(
            public_key=str(public_key),
        )

        return JsonResponse(response)


class UserLogout(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            refresh = request.data.get('refresh', None)

            if refresh is None:
                return HttpResponseBadRequest("Request payload missing refresh token")

            try:
                refresh_token = RefreshToken(refresh)
                refresh_token.blacklist()
            except TokenError:
                return HttpResponse("Invalid token", status=401)

            response = dict(logged_out=True)
            return JsonResponse(response)
        except (json.JSONDecodeError, IntegrityError, TypeError, KeyError, ValueError, FrontendUser.DoesNotExist):
            return HttpResponseBadRequest("Invalid request")


class CheckAuth(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return JsonResponse(dict(is_authenticated=request.user.is_authenticated))


class CreateUser(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            user_email = request.data.get('email')
            user_password = request.data.get('password')

            user_data = dict()
            user_data['id'] = request.data.get('id', uuid.uuid4())
            user_data['is_active'] = str(request.data.get(
                'is_active', 'true')).lower() == 'true'
            user_data['first_name'] = request.data.get('first_name')
            user_data['last_name'] = request.data.get('last_name', None)
            user_data['date_of_birth'] = datetime.strptime(
                request.data.get('date_of_birth'), '%Y-%m-%d').date()

            FrontendUser.objects.create_user(
                user_email, user_password, **user_data)
        except (json.JSONDecodeError, IntegrityError, TypeError, KeyError, ValueError, FrontendUser.DoesNotExist):
            return HttpResponseBadRequest("Invalid request")

        return HttpResponse()


class ChangePassword(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            if not check_password(request.data.get('old_password', ''), request.user.password):
                return HttpResponseForbidden()

            request.user.set_password(request.data.get('new_password'))
            request.user.save()
        except (json.JSONDecodeError, IntegrityError, TypeError, KeyError, ValueError, FrontendUser.DoesNotExist):
            return HttpResponseBadRequest("Invalid request")

        return HttpResponse()


class GetUserData(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return JsonResponse(request.user.asdict())
