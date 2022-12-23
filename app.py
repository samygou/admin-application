#!/usr/bin/python
# encoding: utf-8
"""
@Author: Samy
@File: app.py
@Time: 2022/12/9
@desc: 
"""
import os
import click
import logging

from application import CreateAppX, run_grpc_server


app = CreateAppX().create_app(os.environ.get('ENV_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=app.db, redis=app.redis)


# 不支持命令行启动?
@app.cli.command()
@click.option('-h', type=str)
@click.option('-p', type=int)
@click.option('--host', type=str, help='server host')
@click.option('--port', type=int, help='server port')
def runserver(host, port, h, p):
    server_host = '127.0.0.1'
    server_port = 5000
    if host:
        server_host = host
    if h:
        server_host = h

    if port:
        server_port = port
    if p:
        server_port = p

    app.run(host=server_host, port=server_port)


@app.cli.command()
def create():
    """create db"""
    app.db.create_all()


@app.cli.command()
def drop():
    """Drops database tables"""
    app.db.drop_all()


@app.cli.command()
def recreate():
    """recreate database"""
    drop()
    create()


@app.cli.command()
@click.option('-p', type=int, default=30003, help='grpc server port')
def run_grpc(p):
    """run grpc server"""
    with app.app_context():
        logging.info('run grpc server')
        run_grpc_server(p)


if __name__ == '__main__':
    app.run()
