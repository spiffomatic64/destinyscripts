# destinyscripts
various destiny scripts

For Bungies Destiny api, you will need an API key, you can create one here: https://www.bungie.net/en-us/Application
Once you have it, replace it in the script you are running 
(Ill try to remember to stick to using api_key as the variable name)

Ill dump more stuff here in the future.

Many of these scripts operate on the manifest, to get the manifest, add your API to the manifest.py script, and it should download/extract the manifest file. You should see 2 files afterwards, world.content (zipped) and world_sql_content_4715157a8d3e073dccce96c62e065c67.content (unzipped sqlite db)

You can then use any scripts that operate on the sqlite db (if you see a script that has a filename similar to "world_sql_content_4715157a8d3e073dccce96c62e065c67.content" in it, replace the filename with the one you just downloaded before running)

Example:

C:\Users\spiffomatic64\Downloads\test>manifest.py
{
    "ErrorCode": 1,
    "ErrorStatus": "Success",
    "Message": "Ok",
    "MessageData": {},
    "Response": {
        "mobileAssetContentPath": "/common/destiny2_content/sqlite/asset/asset_sql_content_80b1552f1ba8d0d7d8476b2c6839dcaf.content",
        "mobileClanBannerDatabasePath": "/common/destiny2_content/clanbanner/clanbanner_sql_content_13bcd2427f07d0121bb532a1a0638ba4.content",
        "mobileGearAssetDataBases": [
            {
                "path": "/common/destiny2_content/sqlite/asset/asset_sql_content_80b1552f1ba8d0d7d8476b2c6839dcaf.content",
                "version": 0
            },
            {
                "path": "/common/destiny2_content/sqlite/asset/asset_sql_content_786c2f47cc3ed05b7a132d021b035a76.content",
                "version": 1
            },
            {
                "path": "/common/destiny2_content/sqlite/asset/asset_sql_content_786c2f47cc3ed05b7a132d021b035a76.content",
                "version": 2
            }
        ],
        "mobileGearCDN": {
            "Gear": "/common/destiny2_content/geometry/gear",
            "Geometry": "/common/destiny2_content/geometry/platform/mobile/geometry",
            "PlateRegion": "/common/destiny2_content/geometry/platform/mobile/plated_textures",
            "Shader": "/common/destiny2_content/geometry/platform/mobile/shaders",
            "Texture": "/common/destiny2_content/geometry/platform/mobile/textures"
        },
        "mobileWorldContentPaths": {
            "de": "/common/destiny2_content/sqlite/de/world_sql_content_b4c908fec517df8bb5768d76ab5b4585.content",
            "en": "/common/destiny2_content/sqlite/en/world_sql_content_4715157a8d3e073dccce96c62e065c67.content",
            "es": "/common/destiny2_content/sqlite/es/world_sql_content_01d6a13d27da30b3d6f6d5c3b7c12125.content",
            "es-mx": "/common/destiny2_content/sqlite/es-mx/world_sql_content_82c8184c97063f22cb0440d2e63e81a0.content",
            "fr": "/common/destiny2_content/sqlite/fr/world_sql_content_894daef76218c837458aaa671a83cddb.content",
            "it": "/common/destiny2_content/sqlite/it/world_sql_content_698fb3010750233d142b194c12cab40b.content",
            "ja": "/common/destiny2_content/sqlite/ja/world_sql_content_4fa98910d9780dda3f8c6ef822d3eb22.content",
            "pl": "/common/destiny2_content/sqlite/pl/world_sql_content_be11816204ed5f6b605c666fde0c2c67.content",
            "pt-br": "/common/destiny2_content/sqlite/pt-br/world_sql_content_3637310d7ef5ea0882aaa0c5d3484863.content",
            "ru": "/common/destiny2_content/sqlite/ru/world_sql_content_f8a20ce9ffb54c6ad71bb24daaafacc9.content",
            "zh-cht": "/common/destiny2_content/sqlite/zh-cht/world_sql_content_27ab6410b1197ef7eee4e794be97e58b.content"
        },
        "version": "61252.17.12.02.0200-8"
    },
    "ThrottleSeconds": 0
}
Downloading url: http://bungie.net/common/destiny2_content/sqlite/en/world_sql_content_4715157a8d3e073dccce96c62e065c67.content

C:\Users\spiffomatic64\Downloads\test>secret.py
DestinyEnemyRaceDefinition
DestinyPlaceDefinition
DestinyActivityDefinition
Keep it secret.  Keep it safe.
Keep it secret.  Keep it safe.
Keep it secret.  Keep it safe.
...
