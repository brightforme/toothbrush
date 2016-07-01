#!/usr/bin/env python
import click
import redis

@click.group()
@click.option('-h', '--redis-host', required=True)
@click.option('-a', '--redis-password', required=True)
@click.option('-p', '--redis-port', default=6379)
@click.option('-d', '--redis-db', default=0)
@click.pass_context
def toothbrush(ctx, redis_host, redis_password, redis_port, redis_db):
    ctx.obj = {}
    try:
        ctx.obj['redis_store'] = redis.StrictRedis(host=redis_host,
                                        password=redis_password,
                                        port=redis_port,
                                        db=redis_db,
                                        decode_responses=True)
    except:
        ctx.obj['redis_store'] = None
        click.echo(click.style("Can't reach your redis instance", fg="red", bold=True), err=True)

@toothbrush.command()
@click.option('--app', required=True)
@click.option('--stage', default="production")
@click.pass_context
def list(ctx, app, stage):
    key_in_redis = "{}:{}".format(app,stage)
    env_vars = ctx.obj['redis_store'].hgetall(key_in_redis)
    if not env_vars:
        click.echo(click.style("Can't find this app bruh", fg="blue"), err=True)
    
    for k,v in env_vars.items():
        click.echo(click.style("{} = {}".format(k,v), fg="green"))

@toothbrush.command()
@click.option('--app', required=True)
@click.option('--stage', default="production")
@click.option('--name', required=True)
@click.option('--value', required=True)
@click.pass_context
def set(ctx, app, stage, name, value):
    key_in_redis = "{}:{}".format(app,stage)
    try:
        ctx.obj['redis_store'].hset(key_in_redis, name, value)
    except:
        click.echo(click.style("Something went wrong bruh", fg="red"), err=True)

@toothbrush.command()
@click.option('--app', required=True)
@click.option('--stage', default="production")
@click.option('--name', required=True)
@click.pass_context
def unset(ctx, app, stage, name):
    key_in_redis = "{}:{}".format(app,stage)
    try:
        ctx.obj['redis_store'].hdel(key_in_redis, name)
    except:
        click.echo(click.style("Something went wrong bruh", fg="red"), err=True)

@toothbrush.command()
@click.option('--app', required=True)
@click.option('--stage', default="production")
@click.option('--target', required=True)
@click.option('-n', '--dry-run', is_flag=True)
@click.pass_context
def export(ctx, app, stage, target, dry_run):
    key_in_redis = "{}:{}".format(app,stage)
    env_vars = ctx.obj['redis_store'].hgetall(key_in_redis)
    if not env_vars:
        click.echo(click.style("Can't find this app bruh", fg="blue"), err=True)
    
    with open(target, 'w') as f:
        for k,v in env_vars.items():
            if dry_run:
                click.echo(click.style("export {}={}".format(k,v), fg="green"))
            else:
                f.write("export {}={}\n".format(k,v))
        f.close()

if __name__ == '__main__':
    toothbrush()