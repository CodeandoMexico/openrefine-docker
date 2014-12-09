# import redis
import tutum
from random import random
import logging

logger = logging.getLogger(__name__)

# tutum.user = "miguel_angel"
# tutum.apikey  = ""

SERVICE_NAME = "docker-openrefine"

containers = ["http://" +
              i.public_dns + ":" +
              str(i.container_ports[0]["outer_port"])
                for i in tutum.Container.list(state="Running")
                if i.name == SERVICE_NAME ]


# instances = Dict([zip(i, [False, False]) for i in containers])

def get_session(ip):
    return False

def new_session(ip):
    instance = containers[int(random()  * 10)]
    logger.info("Instancia seleccionada: %s" % instance)
    return instance
