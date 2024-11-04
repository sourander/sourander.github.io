# sourander.github.io

This is an entry portal for all Github Pages site within this account (`sourander.github.io/*`). The data is fetched and updated every night.

## Parsed info

The page info is gathered from two sources.

* The `siteinfo.json` file in the root of the repository. (e.x. [oat/siteinfo.json](https://github.com/sourander/oat/blob/main/siteinfo.json))
* GitHub Repository API. (GET `https://api.github.com/users/sourander/repos`)

The fields and their sources are as follows:

| Field         | Source    | Example                                                               |
| ------------- | --------- | --------------------------------------------------------------------- |
| URL           | API       | [oat](https://sourander.github.io/oat/)                               |
| Description   | API       | Oppimispäiväkirja, Arviointityökalu ja Tilpehööri (OAT)               |
| Latest commit | API       | 2024-10-17                                                            |
| Related repo  | Site Info | [kamk-cookiecutters](https://github.com/sourander/kamk-cookiecutters) |
| Category      | Site Info | Learning tools                                                        |

## Page Info schema

The `pageinfo.json` file in the root of the repository contains the following schema:

```json
{
    "category": "Learning tools",
    "related_repo": "[KAMK Cookiecutters: Oppimispäiväkirja template](https://github.com/sourander/kamk-cookiecutters)"
}
```

Note that each of the fields is optional. If the file is missing altogether, the page will be displayed without the additional info. The default category is "Uncategorized".