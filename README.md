# toothbrush

toothbrush allows you to easily use environment variables for your app. Variables and values are stored in a centralized Redis.

## Usage

List available variables and values:

```shell
toothbrush -h REDIS_HOST -a REDIS_PASSWORD list --app foo --stage production
```

Set a new variable:

```shell
toothbrush -h REDIS_HOST -a REDIS_PASSWORD set --app foo --stage production --name foo --value bar
```

Unset a new variable:

```shell
toothbrush -h REDIS_HOST -a REDIS_PASSWORD unset --app foo --stage production --name foo
```

Load to a file for a new deploy:

```shell
toothbrush -h REDIS_HOST -a REDIS_PASSWORD export --app foo --stage production --target /path/to/your/env/file
```