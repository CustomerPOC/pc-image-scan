# pc-image-scan
Prisma Cloud Container Image Scan Results


## Environment Variables

The following settings should be defined as environment variables. The script will pull these values from the environment and 
use them to authenticate and make API calls against your Prisma Cloud tenant.

 | Name | Type | Description |
 |------|------|-------------|
 | PRISMA_CLOUD_URL | `string` | Your Prisma Cloud URL in the format: https://apiX.prismacloud.io where X is your app stack number
 | PRISMA_CLOUD_IDENTITY | `string` | Username or access key with the ability to access container image scan reports.
 | PRISMA_CLOUD_SECRET | `string` | Password for username or access key above.
 | PRISMA_CLOUD_CONSOLE | `string` | Runtime console path (Runtime -> Manage -> System -> Utilities )


> [!NOTE]
> If you do not use environment variables you will need to set the values for the following manually
> in image_scan_results.py

> [!WARNING]
> Do not store passwords/secrets that are checked into a repo as they will be visible to anyone with access


 | Name | Type | 
 |------|------|
 | url | `string` | 
 | username | `string` |
 | password | `securestring`  |
 | consoleURL | `string` |


## Script Variables


 | Name | Type | Default Value |
 |------|------|-------------|
 | endpoint | `string` | api/v1/images
 | method | `string` | GET
 | body | `string` | {}
 | apiURL | `string` | {consoleURL}/{endpoint}
 | params | `string` | ``` { "limit": 100, "offset": 0 }```


endpoint   = "api/v1/images"
method     = "GET"
body       = {}
apiURL     = f"{consoleURL}/{endpoint}"
params     = {
    "limit": 100,
    "offset": 0
}