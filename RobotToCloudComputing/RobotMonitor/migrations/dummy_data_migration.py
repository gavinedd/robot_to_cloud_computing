from django.db import migrations

from datetime import datetime
import uuid


def populate_robot_data(app_registry, schema_editor):
    Robot = app_registry.get_model('RobotMonitor', 'Robot')
    CsvFile = app_registry.get_model('RobotMonitor', 'CsvFile')
    RobotImageFile = app_registry.get_model('RobotMonitor', 'RobotImageFile')

    robot_data = dict(
        id=uuid.UUID('bf3b4862-d905-4f57-b9ae-2297685d2b8c'),
        name='Spot',
        auth_string='Password1234',
    )

    robot = Robot(**robot_data)
    robot.save()

    csv_file_data = dict(
        id = uuid.UUID('0c5556e9-81f8-4967-a44a-6d29b808d5b8'),
        robot = robot,
        start_timestamp = datetime.utcfromtimestamp(1644100124.938643),
        end_timestamp = datetime.utcfromtimestamp(1644100139.8638778),
        file_path = '/static/csv/Grass_0.csv',
    )

    csv_file_data = dict(
        id = uuid.UUID('0c5556e9-81f8-4967-a44a-6d29b808d5b8'),
        robot = robot,
        start_timestamp = datetime.utcfromtimestamp(1644100127.938643),
        end_timestamp = datetime.utcfromtimestamp(1644100139.8638778),
        file_path = '/static/csv/Grass_0.csv',
    )

    csv_file = CsvFile(**csv_file_data)
    csv_file.save()

    img_files = list()

    img_files.append(dict(
        id = uuid.UUID('98b25f86-1cd8-416e-b276-1b9a08eccc98'),
        image_timestamp = datetime.utcfromtimestamp(1644100131.8507428),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100131.8507428cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('13c25758-000c-4e99-a0b1-4f440c599c72'),
        image_timestamp = datetime.utcfromtimestamp(1644100132.987758),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100132.987758_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('34b1c4d3-5af5-4111-a09b-391a182f9e64'),
        image_timestamp = datetime.utcfromtimestamp(1644100126.9246678),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100126.9246678_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('26071a51-55f6-49c4-8413-4ca1cfead765'),
        image_timestamp = datetime.utcfromtimestamp(1644100130.749728),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100130.749728.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('f5faf967-b02e-43c2-b43b-670fb871f5a9'),
        image_timestamp = datetime.utcfromtimestamp(1644100125.889648),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100125.889648.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('c5a05e39-6267-450d-88fa-e3a81087b59c'),
        image_timestamp = datetime.utcfromtimestamp(1644100139.284873),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100139.284873_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('24b70a0a-2f0a-444a-9816-54c477b8fc97'),
        image_timestamp = datetime.utcfromtimestamp(1644100126.9246678),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100126.9246678cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('0e0a34b2-4296-4d8d-8e94-881150456ea4'),
        image_timestamp = datetime.utcfromtimestamp(1644100125.889648),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100125.889648_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('63f71125-1b13-4111-a8d7-895e90e6d1b1'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.0127878),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100135.0127878.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('9ab2f048-a6e6-49a1-99dd-9719275c9d34'),
        image_timestamp = datetime.utcfromtimestamp(1644100130.749728),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100130.749728_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('bf8f9f1b-bd49-4952-b171-b8dff6da16d3'),
        image_timestamp = datetime.utcfromtimestamp(1644100133.986773),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100133.986773.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('d21c98ea-8004-4313-bde2-124db1263253'),
        image_timestamp = datetime.utcfromtimestamp(1644100129.9667127),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100129.9667127cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('94287c36-5a4d-47d4-b4ee-6a89ccb235c6'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.0127878),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100135.0127878.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('b17d18a9-f86a-4bea-bd85-71d84fb486aa'),
        image_timestamp = datetime.utcfromtimestamp(1644100133.986773),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100133.986773_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('7c010572-253e-4477-a36e-5d7104f467eb'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.906803),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100135.906803_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('210d1f0b-01b4-42d7-a5bb-b9c365e0bacc'),
        image_timestamp = datetime.utcfromtimestamp(1644100126.9246678),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100126.9246678_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('f6c5acc5-6c0b-407d-a0d7-b57a40f18823'),
        image_timestamp = datetime.utcfromtimestamp(1644100131.8507428),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100131.8507428_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('17eae73d-fd82-43ac-bf2b-0d812e05fc6d'),
        image_timestamp = datetime.utcfromtimestamp(1644100132.987758),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100132.987758_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('d89b04ee-40d6-4a68-91cc-979c0dd047fc'),
        image_timestamp = datetime.utcfromtimestamp(1644100139.284873),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100139.284873_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('c8632619-8207-4136-98f2-3129e7bc59af'),
        image_timestamp = datetime.utcfromtimestamp(1644100129.9667127),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100129.9667127cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('6abadf27-2ee1-41e6-8b36-4fe4ffa2b795'),
        image_timestamp = datetime.utcfromtimestamp(1644100137.013818),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100137.013818cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('2733a929-f846-49bf-86d6-b91f7cdf378f'),
        image_timestamp = datetime.utcfromtimestamp(1644100131.8507428),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100131.8507428cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('7e561650-95a4-44f6-8a44-a7b69a085eec'),
        image_timestamp = datetime.utcfromtimestamp(1644100125.889648),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100125.889648_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('1ebafaba-f027-458d-99d5-272d71a79475'),
        image_timestamp = datetime.utcfromtimestamp(1644100132.987758),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100132.987758.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('05fdacd1-2fde-4a5e-b9a2-4f9d367742ac'),
        image_timestamp = datetime.utcfromtimestamp(1644100139.284873),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100139.284873cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('b4464cea-d91d-498e-b79e-8458dee2a1bc'),
        image_timestamp = datetime.utcfromtimestamp(1644100131.8507428),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100131.8507428_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('a17d6373-20eb-43c4-b32e-e1f3066a0a6f'),
        image_timestamp = datetime.utcfromtimestamp(1644100133.986773),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100133.986773_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('720a0b3e-05f2-40ce-aa99-fef100b5a3dd'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.906803),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100135.906803_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('08fab2e8-cf83-4123-a684-a486f01b8a81'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.906803),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100135.906803.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('728f45ab-b684-4bf7-9862-c105478ed3c4'),
        image_timestamp = datetime.utcfromtimestamp(1644100130.749728),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100130.749728_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('1f59a2d3-b99d-44fc-83bd-5faf50eb31f8'),
        image_timestamp = datetime.utcfromtimestamp(1644100126.9246678),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100126.9246678cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('0a522953-fc5e-4ea7-ace6-030d8a2f0e72'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.0127878),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100135.0127878cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('8017fef8-4c48-4148-8540-a14a7fd6a563'),
        image_timestamp = datetime.utcfromtimestamp(1644100139.284873),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100139.284873.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('4d775fac-0a74-4d33-9943-15de6afda2a8'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.0127878),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100135.0127878_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('690f5a23-32bb-458d-9630-d63a22e0565f'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.0127878),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100135.0127878_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('3ddaa74c-873e-4218-b5e0-eb03ed0d5e57'),
        image_timestamp = datetime.utcfromtimestamp(1644100137.013818),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100137.013818.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('5e8964f6-d17f-4453-90ab-62b7046d6789'),
        image_timestamp = datetime.utcfromtimestamp(1644100132.987758),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100132.987758cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('273797d0-8293-49d4-b32c-359db540561d'),
        image_timestamp = datetime.utcfromtimestamp(1644100138.018833),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100138.018833_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('4a96a91a-8f19-4232-83fc-c40cbf2edbbd'),
        image_timestamp = datetime.utcfromtimestamp(1644100133.986773),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100133.986773cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('223b7e3a-66f8-4325-b7ac-ef48e4e38d04'),
        image_timestamp = datetime.utcfromtimestamp(1644100128.9346929),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100128.9346929.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ee8482da-5240-4815-b334-51df0fcfed7d'),
        image_timestamp = datetime.utcfromtimestamp(1644100127.926683),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100127.926683.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('2c41af45-4c6c-41fe-a283-beead2fe563f'),
        image_timestamp = datetime.utcfromtimestamp(1644100127.926683),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100127.926683cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('b0c3a11f-fdd1-493b-ac3e-98b1b22b4b6e'),
        image_timestamp = datetime.utcfromtimestamp(1644100125.889648),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100125.889648cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('e855f5cb-f8c6-4c9b-8fe2-475e303afb82'),
        image_timestamp = datetime.utcfromtimestamp(1644100128.9346929),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100128.9346929.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('afdf74b7-5a49-480d-ab2a-6c01f4eea29c'),
        image_timestamp = datetime.utcfromtimestamp(1644100130.749728),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100130.749728cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('10ce53e4-a21a-4b7a-8a31-cf254cc1d716'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.0127878),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100135.0127878cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('744070e6-5861-4e5b-a74e-162a3c689993'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.906803),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100135.906803cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('2ee3b7eb-6438-496b-8032-283c8be0f737'),
        image_timestamp = datetime.utcfromtimestamp(1644100138.018833),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100138.018833.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('f929f644-85d8-49b4-bff4-4b00d6727422'),
        image_timestamp = datetime.utcfromtimestamp(1644100138.018833),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100138.018833cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ce7ae718-deb1-493f-ad78-5a84a1a0512e'),
        image_timestamp = datetime.utcfromtimestamp(1644100138.018833),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100138.018833_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('baa2e69a-b1dc-4ded-b640-9cbe631dc3c8'),
        image_timestamp = datetime.utcfromtimestamp(1644100125.889648),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100125.889648cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('d4b99ac0-fecd-4225-ba57-d6c34f022ff3'),
        image_timestamp = datetime.utcfromtimestamp(1644100129.9667127),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100129.9667127_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('b25a9f10-79ee-4251-b334-a5335ed2b830'),
        image_timestamp = datetime.utcfromtimestamp(1644100131.8507428),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100131.8507428.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('718703ba-92f0-474d-b5fd-63f32c330305'),
        image_timestamp = datetime.utcfromtimestamp(1644100127.926683),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100127.926683cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('e9b7280c-1bad-4280-9760-6ff0551d2fc2'),
        image_timestamp = datetime.utcfromtimestamp(1644100131.8507428),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100131.8507428.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('1cedd251-926a-4d55-95b8-acb098fd8f27'),
        image_timestamp = datetime.utcfromtimestamp(1644100138.018833),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100138.018833cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('edfafa02-37e2-41e5-9248-a613200d6fee'),
        image_timestamp = datetime.utcfromtimestamp(1644100132.987758),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100132.987758.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('e9e47c98-6dcb-4849-ba92-93648e56d867'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.906803),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100135.906803cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('5181d3d0-3e7c-462c-91f5-50f67d93c3c4'),
        image_timestamp = datetime.utcfromtimestamp(1644100126.9246678),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100126.9246678.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('352a4e08-1762-4a1e-94e2-dcdbd2e357f3'),
        image_timestamp = datetime.utcfromtimestamp(1644100126.9246678),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100126.9246678.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('eaef1260-bc93-4349-a179-ecc946488354'),
        image_timestamp = datetime.utcfromtimestamp(1644100130.749728),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100130.749728cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('daba99dc-7d56-4909-aea1-1c5fd0be1e66'),
        image_timestamp = datetime.utcfromtimestamp(1644100129.9667127),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100129.9667127_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('5c5c30ec-1fda-4d3c-a2fd-7b4c89c9c5b0'),
        image_timestamp = datetime.utcfromtimestamp(1644100137.013818),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1644100137.013818_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('05225805-33b5-4469-a84f-2594197b2acc'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.906803),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100135.906803.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('98ab748b-9bfa-4a27-a28d-12e93ae4b77a'),
        image_timestamp = datetime.utcfromtimestamp(1644100130.749728),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1644100130.749728.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('aa678ec7-47c8-4d5e-a7b1-77818d0eec58'),
        image_timestamp = datetime.utcfromtimestamp(1644100125.889648),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100125.889648.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('d6a3bb32-de82-4fd2-97e7-d65af8b648f4'),
        image_timestamp = datetime.utcfromtimestamp(1644100133.986773),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1644100133.986773cv_depth.jpg',
    ))

    for f in img_files:
        robot_image_file = RobotImageFile(**f)
        robot_image_file.save()


class Migration(migrations.Migration):
    dependencies = [('RobotMonitor', '0001_initial')]

    operations = [
        migrations.RunPython(populate_robot_data),
    ]
