# import redis
import tutum
from random import random
import logging
from os import getenv

logger = logging.getLogger(__name__)

# tutum.user = "miguel_angel"
# tutum.apikey  = ""


SERVICE_NAME = getenv("TUTUM_SERVICE", "openrefine-geturl")
# instances = Dict([zip(i, [False, False]) for i in containers])

def get_session(ip):
    return False

def new_session(ip):
    containers = ["http://refinadora.datamx.io:" +
              str(i.container_ports[0]["outer_port"])
                for i in tutum.Container.list(state="Running")
                if SERVICE_NAME in i.name]

    instance = containers[int(random()  * len(containers))]
    logger.info("Instancia seleccionada: %s" % instance)
    return instance
