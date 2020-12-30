# Comic Vine API Findings

Comic Vine API: https://comicvine.gamespot.com/api

The API docs are decent but it's not super detailed and I have to figure things out from forums/blogs. Dumping what I know here:

## UNderstanding Id's
Comic Vine seems to categorize all their content using a 2 part id:
```
<content_type_id>-<content_id> // ex: 4050-85776
```

- `content_type_id`: Think things like comics series, series, comic issue, publisher, etc.
    - `4050` - Seems to be "comic series". ex: https://comicvine.gamespot.com/monstress/4050-85776/
    - `4000` - Seems to be "comic issue". ex: https://comicvine.gamespot.com/monstress-1/4000-504982/
    - `4010` - Seems to be "publisher". ex https://comicvine.gamespot.com/image/4010-513/
- `content_id` - Actual content's unique id. This seems to be the property `id` in the response from endpoints like `/volumes`, `/publishers`. ex: 85776

## Endpoint Usages
Just how I'm using certain endpoints to get certain info. May not be the best usage, but it works for what I need!

- `/volumes` - Search for a series. Example: x-men, monstress
- `/issues` - Search for issues in a series. Useful since it can get all issues and includes store release dates!
