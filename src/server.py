#!/usr/bin/env python

from __init__ import app, register_service
import os

from RDS import Util, LoginService, FileTransferMode, FileTransferArchive
service = LoginService(
    servicename="port-cdstar",
    implements=["metadata"],
    fileTransferMode=FileTransferMode.passive,
    fileTransferArchive=FileTransferArchive.none,
    userId=False,
    password=False,
    description={"en": "CDSTAR (Common Data Storage ARchitecture) is a head-less data repository and framework for research data management applications. The goal is to provide a rich set of common functionality (scalable storage, publishing, archiving, metadata annotations, access management and search) as a web-service for other applications to build upon, and to simplify the rapid development of highly customized tools and workflows for data-heavy research applications.",
                 "de": "CDSTAR (Common Data Storage ARchitecture) ist ein kopfloser Datenspeicher und ein Rahmen für Anwendungen zur Verwaltung von Forschungsdaten. Ziel ist es, einen umfangreichen Satz gemeinsamer Funktionen (skalierbare Speicherung, Veröffentlichung, Archivierung, Metadaten-Anmerkungen, Zugriffsverwaltung und Suche) als Webdienst bereitzustellen, auf dem andere Anwendungen aufbauen können, und die rasche Entwicklung hochgradig angepasster Werkzeuge und Arbeitsabläufe für datenintensive Forschungsanwendungen zu vereinfachen."},
    infoUrl="https://docs.gwdg.de/doku.php?id=en:start",
    helpUrl="https://docs.gwdg.de/doku.php?id=en:services:storage_services:gwdg_cdstar:start",
    icon="./datasafe.svg",
    displayName="CDStar",
)
Util.register_service(service)

# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
app.run(port=8080, server="gevent")
