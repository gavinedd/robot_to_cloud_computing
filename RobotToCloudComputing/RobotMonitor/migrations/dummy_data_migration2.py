from django.db import migrations

from datetime import datetime
import uuid


def populate_robot_data(app_registry, schema_editor):
    Robot = app_registry.get_model('RobotMonitor', 'Robot')
    CsvFile = app_registry.get_model('RobotMonitor', 'CsvFile')
    RobotImageFile = app_registry.get_model('RobotMonitor', 'RobotImageFile')

    spot = Robot.objects.get(pk='bf3b4862-d905-4f57-b9ae-2297685d2b8c')
    csv_file_data = dict(
        id = uuid.UUID('ddf9b53a-e053-480f-830f-8a545eb795df'),
        robot = spot,
        start_timestamp = datetime.utcfromtimestamp(1650935790.699352),
        end_timestamp = datetime.utcfromtimestamp(1650935791.6593819),
        file_path = '/static/csv/None_0.csv',
    )

    csv_file = CsvFile(**csv_file_data)
    csv_file.save()

    img_files = list()

    img_files.append(dict(
        id = uuid.UUID('42b47a85-3b04-4853-a695-0d2bfcb5d220'),
        image_timestamp = datetime.utcfromtimestamp(1650934389.093662),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1650934389.093662.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('0fbafe50-7f15-4c90-a20b-5c57946d2ab2'),
        image_timestamp = datetime.utcfromtimestamp(1650934389.093662),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1650934389.093662_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('47ace047-cd41-4cd9-a42b-5e347cd9e5c1'),
        image_timestamp = datetime.utcfromtimestamp(1650934389.093662),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1650934389.093662cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('2deb825b-1f07-4115-8c7b-094288ebf35c'),
        image_timestamp = datetime.utcfromtimestamp(1650934736.135717),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1650934736.135717.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('a77276df-8962-419a-b3b6-d73ac9f8cbcc'),
        image_timestamp = datetime.utcfromtimestamp(1650934736.135717),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1650934736.135717_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('02a0aba5-b974-4f69-b2f5-a3fb90948d45'),
        image_timestamp = datetime.utcfromtimestamp(1650934736.135717),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1650934736.135717cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('303d23c4-c45c-4e19-b07a-7cd723a2542e'),
        image_timestamp = datetime.utcfromtimestamp(1650934737.131742),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1650934737.131742.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('5c955f50-5a48-471b-b394-6e8bfc905328'),
        image_timestamp = datetime.utcfromtimestamp(1650934737.131742),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1650934737.131742_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('4e148400-1c55-43a4-92c1-7b7bbe3e406a'),
        image_timestamp = datetime.utcfromtimestamp(1650934737.131742),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1650934737.131742cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('c38ab422-9075-49bb-b29e-35e48aa2c034'),
        image_timestamp = datetime.utcfromtimestamp(1650935203.014632),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1650935203.014632.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('2e9bc787-9f5b-47a2-a9a4-bbebf20a423a'),
        image_timestamp = datetime.utcfromtimestamp(1650935203.014632),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1650935203.014632_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('79b1867d-e188-4d87-8a6d-befc4fa2cd3b'),
        image_timestamp = datetime.utcfromtimestamp(1650935203.014632),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1650935203.014632cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('e855ab75-a598-4730-9e46-a417fd8eed3d'),
        image_timestamp = datetime.utcfromtimestamp(1650935572.617157),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1650935572.617157.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('dfe3ad4f-cf3f-4d0e-8973-fa3054388d0c'),
        image_timestamp = datetime.utcfromtimestamp(1650935572.617157),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1650935572.617157_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('0a17b927-51ea-4a72-966a-fd4ea09ec35c'),
        image_timestamp = datetime.utcfromtimestamp(1650935572.617157),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1650935572.617157cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('275acfc1-c2a0-40ae-a2ee-cc627f7ad30c'),
        image_timestamp = datetime.utcfromtimestamp(1650935573.6191769),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1650935573.6191769.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('15498d73-9fdd-48d5-88e0-89525ca732b3'),
        image_timestamp = datetime.utcfromtimestamp(1650935573.6191769),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1650935573.6191769_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('af839290-69c8-4d09-aaed-28db63509531'),
        image_timestamp = datetime.utcfromtimestamp(1650935573.6191769),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1650935573.6191769cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('57485a80-3569-4d70-9e8c-1e6fc9198652'),
        image_timestamp = datetime.utcfromtimestamp(1650935574.618187),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1650935574.618187.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('728b2a81-ea1a-4204-b77c-09616eb61b7f'),
        image_timestamp = datetime.utcfromtimestamp(1650935574.618187),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1650935574.618187_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('1c727bff-cf7f-4e4d-84ae-d2af88d78787'),
        image_timestamp = datetime.utcfromtimestamp(1650935574.618187),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1650935574.618187cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('8394f44f-f562-4add-994f-26dccc602d7a'),
        image_timestamp = datetime.utcfromtimestamp(1650935575.638207),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1650935575.638207.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ef3600bb-5439-40db-acf4-917ea40c43ac'),
        image_timestamp = datetime.utcfromtimestamp(1650935575.638207),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1650935575.638207_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('699a2621-c385-47d9-9356-47a693e3f701'),
        image_timestamp = datetime.utcfromtimestamp(1650935575.638207),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1650935575.638207cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('96b507e9-b30b-4180-9d2d-71de07bb54cf'),
        image_timestamp = datetime.utcfromtimestamp(1650935791.6593819),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/left_1650935791.6593819.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('8143685c-8390-4420-b97b-b60d2a18995c'),
        image_timestamp = datetime.utcfromtimestamp(1650935791.6593819),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/left_1650935791.6593819_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('afae078d-cc5f-4f72-8fa0-ac60aa47f916'),
        image_timestamp = datetime.utcfromtimestamp(1650935791.6593819),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/left_1650935791.6593819cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ca0b3ea0-d683-4368-82d7-66f2def1ecac'),
        image_timestamp = datetime.utcfromtimestamp(1644100125.889648),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100125.889648.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('48e912f6-7ee1-4a1f-9bda-b13507b3d80b'),
        image_timestamp = datetime.utcfromtimestamp(1644100125.889648),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100125.889648_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('eb0e2371-263d-45ce-a673-85a3ec47e223'),
        image_timestamp = datetime.utcfromtimestamp(1644100125.889648),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100125.889648cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('c7ad7d6c-aabf-42c0-ad4f-b5e10e509985'),
        image_timestamp = datetime.utcfromtimestamp(1644100126.9246678),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100126.9246678.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('651bf8c2-47ee-4b66-99eb-74599a1c4bbd'),
        image_timestamp = datetime.utcfromtimestamp(1644100126.9246678),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100126.9246678_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('27fe82e3-e63f-4b45-b471-ac5519b7661f'),
        image_timestamp = datetime.utcfromtimestamp(1644100126.9246678),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100126.9246678cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('02a2886b-eec4-4c15-a5c9-a58a28929492'),
        image_timestamp = datetime.utcfromtimestamp(1644100127.926683),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100127.926683.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('8dc5dd18-9026-4c85-9666-437039e98138'),
        image_timestamp = datetime.utcfromtimestamp(1644100127.926683),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100127.926683_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('9cdc49b6-2c89-4642-941a-123beeba1594'),
        image_timestamp = datetime.utcfromtimestamp(1644100127.926683),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100127.926683cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('8e47953c-b4b0-4715-b60c-555ce16561b5'),
        image_timestamp = datetime.utcfromtimestamp(1644100128.9346929),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100128.9346929.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('2e46a249-1148-4958-b324-4b23aa81456d'),
        image_timestamp = datetime.utcfromtimestamp(1644100128.9346929),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100128.9346929_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('b47a36dd-86ff-4ad9-83b6-05e03b19055d'),
        image_timestamp = datetime.utcfromtimestamp(1644100128.9346929),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100128.9346929cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('fb0db2f7-70f4-4b67-8837-34c18afa283e'),
        image_timestamp = datetime.utcfromtimestamp(1644100129.9667127),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100129.9667127.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('f12b3e5b-2183-41e3-89d0-28f7d8fe9028'),
        image_timestamp = datetime.utcfromtimestamp(1644100129.9667127),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100129.9667127_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ee6a00ba-afda-48b3-8bee-07023832dad0'),
        image_timestamp = datetime.utcfromtimestamp(1644100129.9667127),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100129.9667127cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('3d2e00a0-d3c8-41b7-9813-b04cf50e3473'),
        image_timestamp = datetime.utcfromtimestamp(1644100130.749728),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100130.749728.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('fd6895ec-75b4-418a-bc89-760ef7d2f836'),
        image_timestamp = datetime.utcfromtimestamp(1644100130.749728),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100130.749728_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('87ed4ee4-c0fb-4383-84bd-fcd227e7e38f'),
        image_timestamp = datetime.utcfromtimestamp(1644100130.749728),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100130.749728cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ff281975-151a-4974-ab1b-75f43af2d4f4'),
        image_timestamp = datetime.utcfromtimestamp(1644100131.8507428),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100131.8507428.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('0b4035e7-3ae7-4f7e-b689-e7d9e19244b1'),
        image_timestamp = datetime.utcfromtimestamp(1644100131.8507428),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100131.8507428_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('d4d334ac-f605-41f2-b453-b832852034a2'),
        image_timestamp = datetime.utcfromtimestamp(1644100131.8507428),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100131.8507428cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('45aa6385-7e39-4ab1-bd0e-0e9d35a91a08'),
        image_timestamp = datetime.utcfromtimestamp(1644100132.987758),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100132.987758.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('7b8baa65-23d5-4dab-992c-083394144964'),
        image_timestamp = datetime.utcfromtimestamp(1644100132.987758),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100132.987758_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('8df5ddfc-caf4-4595-aa25-ef57774e1d27'),
        image_timestamp = datetime.utcfromtimestamp(1644100132.987758),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100132.987758cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('5ac6b0c6-9e7a-405b-aeca-63a1c8cbec95'),
        image_timestamp = datetime.utcfromtimestamp(1644100133.986773),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100133.986773.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('d795c35e-fb37-4b50-9d04-c498bea37b65'),
        image_timestamp = datetime.utcfromtimestamp(1644100133.986773),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100133.986773_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('72f2c5fa-f12f-4478-b820-5aa6caea318b'),
        image_timestamp = datetime.utcfromtimestamp(1644100133.986773),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100133.986773cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ec5558e9-48af-40ec-b15a-0f4ed12ecc27'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.0127878),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100135.0127878.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('257b0143-7c2e-444a-a1e3-f429beec833a'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.0127878),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100135.0127878_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('8ec1d223-3276-4928-94cc-74d003f15f22'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.0127878),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100135.0127878cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('9ecbeb69-51c3-4a66-90ba-b43c3ee8a8b5'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.906803),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100135.906803.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('5730cef1-6cc1-436c-9dc1-ba1867735fe2'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.906803),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100135.906803_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('196fd3b7-1e32-4538-ae39-e754f02587c1'),
        image_timestamp = datetime.utcfromtimestamp(1644100135.906803),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100135.906803cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('67cdc435-8903-4815-9246-12e3b73e5952'),
        image_timestamp = datetime.utcfromtimestamp(1644100137.013818),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100137.013818.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('77aa8819-a469-47de-8d67-cbbfd4008331'),
        image_timestamp = datetime.utcfromtimestamp(1644100137.013818),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100137.013818_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('15245849-9810-4ae8-9f8b-b135476dd4be'),
        image_timestamp = datetime.utcfromtimestamp(1644100137.013818),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100137.013818cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('cc542130-794e-4fad-babe-8978ad1318e7'),
        image_timestamp = datetime.utcfromtimestamp(1644100138.018833),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100138.018833.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('55bc680f-7958-4fea-ae21-146806647664'),
        image_timestamp = datetime.utcfromtimestamp(1644100138.018833),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100138.018833_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('93e4714e-b9dc-476b-9d36-ac5b688999fb'),
        image_timestamp = datetime.utcfromtimestamp(1644100138.018833),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100138.018833cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ad723c54-0859-44e2-b763-da2d1fee081c'),
        image_timestamp = datetime.utcfromtimestamp(1644100139.284873),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1644100139.284873.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('984a506a-ccfc-4dfe-b2e9-b341d78430d1'),
        image_timestamp = datetime.utcfromtimestamp(1644100139.284873),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1644100139.284873_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('24e6278a-34af-4e86-a667-bcd43862a188'),
        image_timestamp = datetime.utcfromtimestamp(1644100139.284873),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1644100139.284873cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('900ce480-3848-40c4-b08d-9a040d477dd5'),
        image_timestamp = datetime.utcfromtimestamp(1650934389.093662),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1650934389.093662.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('33e78e9f-9c8f-4af1-9dc0-7145e88663ba'),
        image_timestamp = datetime.utcfromtimestamp(1650934389.093662),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1650934389.093662_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('7bf0b53c-7e32-490c-863e-74728311cc72'),
        image_timestamp = datetime.utcfromtimestamp(1650934389.093662),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1650934389.093662cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('01d880d0-104f-48d9-af56-f842bd6c835d'),
        image_timestamp = datetime.utcfromtimestamp(1650934736.135717),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1650934736.135717.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('01d5ab09-8b81-4579-b0b6-7e7c9ddf0e60'),
        image_timestamp = datetime.utcfromtimestamp(1650934736.135717),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1650934736.135717_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('b0250cf1-9bd6-4d9c-89a2-8ae5012c8456'),
        image_timestamp = datetime.utcfromtimestamp(1650934736.135717),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1650934736.135717cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('653f348e-3c68-4871-9f57-ce3313dc18aa'),
        image_timestamp = datetime.utcfromtimestamp(1650934737.131742),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1650934737.131742.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('31bd01f2-cc66-4451-a012-b4e2a8ff003b'),
        image_timestamp = datetime.utcfromtimestamp(1650934737.131742),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1650934737.131742_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ec8e1fbd-3782-4cdc-aafb-e20072f4284e'),
        image_timestamp = datetime.utcfromtimestamp(1650934737.131742),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1650934737.131742cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ea8f52f2-6974-4f91-9c1a-4c1d40357d14'),
        image_timestamp = datetime.utcfromtimestamp(1650935203.014632),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1650935203.014632.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('d34b3fa8-56a1-4426-bff5-e17b2d56c325'),
        image_timestamp = datetime.utcfromtimestamp(1650935203.014632),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1650935203.014632_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('865f261f-424d-491e-a33a-42c9e964583d'),
        image_timestamp = datetime.utcfromtimestamp(1650935203.014632),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1650935203.014632cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('5eae7cb0-6dc2-4c9b-9d1c-db8a963ff1ef'),
        image_timestamp = datetime.utcfromtimestamp(1650935572.617157),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1650935572.617157.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('224b9d38-d8ef-467a-85c6-c27448800b56'),
        image_timestamp = datetime.utcfromtimestamp(1650935572.617157),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1650935572.617157_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('e401cf96-3682-451e-ae5f-408cb8dc96aa'),
        image_timestamp = datetime.utcfromtimestamp(1650935572.617157),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1650935572.617157cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('1b666766-ee30-4699-af3c-3aec6ccef3f0'),
        image_timestamp = datetime.utcfromtimestamp(1650935573.6191769),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1650935573.6191769.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('d4063ad4-1449-417f-a8b1-cd80608433c8'),
        image_timestamp = datetime.utcfromtimestamp(1650935573.6191769),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1650935573.6191769_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('660b8015-ba36-4cd1-b7b2-41e70fc28e56'),
        image_timestamp = datetime.utcfromtimestamp(1650935573.6191769),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1650935573.6191769cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('dc0b4d17-5f4a-4bfa-a3c0-87764c47ae7d'),
        image_timestamp = datetime.utcfromtimestamp(1650935574.618187),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1650935574.618187.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('df04aa12-ad85-4ad5-8dd2-6944baa5f208'),
        image_timestamp = datetime.utcfromtimestamp(1650935574.618187),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1650935574.618187_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('fb1c651c-7e7a-4740-a9f3-b7238263df1a'),
        image_timestamp = datetime.utcfromtimestamp(1650935574.618187),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1650935574.618187cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('a291773b-9095-4a59-8e3b-9904fbdef249'),
        image_timestamp = datetime.utcfromtimestamp(1650935575.638207),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1650935575.638207.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('14fbb723-c96d-4f88-bb38-289158d077ca'),
        image_timestamp = datetime.utcfromtimestamp(1650935575.638207),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1650935575.638207_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('13becfe0-a047-4f95-a104-a517fb3f8337'),
        image_timestamp = datetime.utcfromtimestamp(1650935575.638207),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1650935575.638207cv_depth.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('766b8b90-15be-4a32-a427-9b69488aaf58'),
        image_timestamp = datetime.utcfromtimestamp(1650935791.6593819),
        csv_file = csv_file,
        image_type = 'infrared',
        file_path = '/static/images/right_1650935791.6593819.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('ca804ecd-f672-4bfa-bcba-b55910c78503'),
        image_timestamp = datetime.utcfromtimestamp(1650935791.6593819),
        csv_file = csv_file,
        image_type = 'visual_rgb',
        file_path = '/static/images/right_1650935791.6593819_visual_rgb.jpg',
    ))
    img_files.append(dict(
        id = uuid.UUID('de804ecd-f672-4bfa-bcba-b55910c7850a'),
        image_timestamp = datetime.utcfromtimestamp(1650935791.6593819),
        csv_file = csv_file,
        image_type = 'cv_depth',
        file_path = '/static/images/right_1650935791.6593819cv_depth.jpg',
    ))

    for f in img_files:
        robot_image_file = RobotImageFile(**f)
        robot_image_file.save()

    
class Migration(migrations.Migration):
    dependencies = [('RobotMonitor', '0001_initial'), ('RobotMonitor', 'dummy_data_migration')]

    operations = [
        migrations.RunPython(populate_robot_data),
    ]
