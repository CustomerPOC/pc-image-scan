# Prisma Cloud Container Image Scan Results

This script can be used to return all container image scan results from Prisma Cloud in JSON format.

- [Setup](#setup)
- [Script Files](#script-files)
- [Script Variables](#script-variables)

-----

## Setup

1. Clone this repo to your local system

    ```shell
    git clone https://github.com/CustomerPOC/pc-image-scan.git
    ```

2. Create the following environment variables on your local system

    | Name | Type | Description |
    |------|------|-------------|
    | PRISMA_CLOUD_URL | `string` | Your Prisma Cloud URL in the format: https://apiX.prismacloud.io where X is your app stack number
    | PRISMA_CLOUD_IDENTITY | `string` | Username or access key with the ability to access container image scan reports.
    | PRISMA_CLOUD_SECRET | `string` | Password for username or access key above.
    | PRISMA_CLOUD_CONSOLE | `string` | Runtime console path (Runtime -> Manage -> System -> Utilities )

> [!NOTE]
> If you do not use environment variables you will need to set the [values](#script-variables) 
> manually by editing image_scan_results.py for all variables using `os.getenv`


3. Run the script to return results

    ```shell
    python3 ./image_scan_results.py
    ```

> [!NOTE]
> This API generates a lot of data. 1000 images returned will result in a file that is ~300MB in size. 


## Script Files

There are only 2 files used by this script, functions that returns an auth token and provides 2 other functions for calculating the size
of the response, and image_scan_results that query the API to return results and write them to a timestamped file.

 | Name | Purpose | 
 |------|------|
 | [functions.py](./Python/functions.py) | Authenticate against the Prisma Cloud API to return a bearer token for API requests | 
 | [image_scan_results.py](./Python/image_scan_results.py) | Return all container image scan results |
 

## Script Variables

The following variables are used inside of the script to return results. The params variable sets the returned limit to 100 (maximum) and the offset to 0 (start of request). The limit and offset can both be adjusted, but offset is set automatically by the script to increment and return all results. If there is a specific result you want to return and you know the offset you can pull just that image using a limit of 1 and the appropriate offset value.


 | Name | Type | Default Value |
 |------|------|-------------|
 | url | `string` | os.getenv("PRISMA_CLOUD_URL")
 | username | `string` | os.getenv("PRISMA_CLOUD_SECRET")
 | password | `securestring` | os.getenv("PRISMA_CLOUD_IDENTITY")
 | consoleURL | `string` | os.getenv("PRISMA_CLOUD_CONSOLE")
 | timestamp | `string` | datetime.now().strftime('%Y%m%d_%H%M%S')
 | fileName | `string` | scan_results_{timestamp}.json
 | endpoint | `string` | api/v1/images
 | method | `string` | GET
 | body | `string` | {}
 | apiURL | `string` | {consoleURL}/{endpoint}
 | params | `string` | ``` { "limit": 100, "offset": 0 }```
