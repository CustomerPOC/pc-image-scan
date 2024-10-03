# pc-image-scan
Prisma Cloud Container Image Scan Results


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

---

 | Name | Type | 
 |------|------|
 | url | `string` | 
 | username | `string` |
 | password | `securestring`  |
 | consoleURL | `string` |


> [!WARNING]
> Do not store passwords/secrets that are checked into a repo as they will be visible to anyone with access


## Script Variables

The following variables are used inside of the script to return results. The params variable sets the returned limit to 100 (maximum) and the offset to 0. The limit and offset can both be adjusted, but offset is set automatically by the script to increment and return all results. If there is a specific result you want to return and you know the offset you can pull just that image using a limit of 1 and the appropriate offset value.


 | Name | Type | Default Value |
 |------|------|-------------|
 | endpoint | `string` | api/v1/images
 | method | `string` | GET
 | body | `string` | {}
 | apiURL | `string` | {consoleURL}/{endpoint}
 | params | `string` | ``` { "limit": 100, "offset": 0 }```


## Notes

This script stores the returned data in a variable named all_results. This data only exists at script runtime. If you want to see the results on the screen you can add the following line to the bottom of the script:

```python
print(all_results)
```

> [!WARNING]
> This API endpoint generates a lot of data. As an example, returning just 10 images results in ~4MB of data. 
> 1000 images would generate a response that is ~400MB. 