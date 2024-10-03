# Prisma Cloud Container Image Scan Results

This script can be used to return all container image scan results in JSON format.

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
> If you do not use environment variables you will need to set the values for the following
> by editing image_scan_results.py

        - url 
        - username 
        - password  
        - consoleURL 
 

> [!WARNING]
> Do not store passwords/secrets that are checked into a repo as they will be visible to anyone with access


3. Run the script to return results

    ```shell
    python3 ./image_scan_results.py
    ```

> [!WARNING]
> This API generates a lot of data. 1000 images returned will result in a file that is ~300MB in size. 


## Files

 | Name | Purpose | 
 |------|------|
 | functions.py | Authenticate against the Prisma Cloud API to return a bearer token for API requests | 
 | image_scan_results.py | Return all container image scan results |
 

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

### Variables set with Environment Variables

 | Name | Type | 
 |------|------|
 | url | `string` | 
 | username | `string` |
 | password | `securestring`  |
 | consoleURL | `string` |





## Script Variables

The following variables are used inside of the script to return results. The params variable sets the returned limit to 100 (maximum) and the offset to 0 (start of request). The limit and offset can both be adjusted, but offset is set automatically by the script to increment and return all results. If there is a specific result you want to return and you know the offset you can pull just that image using a limit of 1 and the appropriate offset value.


 | Name | Type | Default Value |
 |------|------|-------------|
 | timestamp | `string` | datetime.now().strftime('%Y%m%d_%H%M%S')
 | fileName | `string` | scan_results_{timestamp}.json
 | endpoint | `string` | api/v1/images
 | method | `string` | GET
 | body | `string` | {}
 | apiURL | `string` | {consoleURL}/{endpoint}
 | params | `string` | ``` { "limit": 100, "offset": 0 }```


