import sys
import argparse
import requests
import xml.etree.ElementTree as ET

JENKINS_BASE_URL = "http://localhost:8080"
JENKINS_PLUGIN_MANAGER_PATH = "pluginManager/api/xml?depth=1"
DEFAULT_CHUNK_SIZE = 20
TAGS = {
    "VERSION": "version",
    "SHORT_NAME": "shortName"
}


def main():
    arg_parser = argparse.ArgumentParser(
        prog="list-jenkins-plugins",
        description="snapshot list of installed plugins on a Jenkins instance in plugins.txt format"
    )
    arg_parser.add_argument(
        "jenkins_base_url",
        nargs="?",
        default=JENKINS_BASE_URL,
        help="Jenkins instance base url. Defaults to {}".format(JENKINS_BASE_URL)
    ),
    arg_parser.add_argument(
        "--user", "-u",
        default=""
    ),
    arg_parser.add_argument(
        "--password", "-p",
        default=""
    ),
    arg_parser.add_argument(
        "--chunk-size", "-c",
        type=int,
        default=DEFAULT_CHUNK_SIZE,
        help="Jenkins response streaming chunks size. Defaults to {} kB".format(DEFAULT_CHUNK_SIZE)
    )
    args = arg_parser.parse_args()
    return parse_xml_plugins_list(args.jenkins_base_url, args.chunk_size, (args.user, args.password))


def parse_xml_plugins_list(jenkins_base_url, chunk_size, auth):
    chunk_size = chunk_size * 1024
    xml_pull_parser = ET.XMLPullParser()
    plugins = []

    with requests.get(
            "{jenkins_base_url}/{path}".format(jenkins_base_url=jenkins_base_url, path=JENKINS_PLUGIN_MANAGER_PATH),
            auth=auth,
            stream=True
    ) as jenkins_response:
        # parse the xml plugins list a chunk at a time, a very large set of plugins may be installed
        for chunk in jenkins_response.iter_content(chunk_size):
            if chunk:
                xml_pull_parser.feed(chunk)
                try:
                    for event, element in xml_pull_parser.read_events():
                        """
                        Rely on the fact that a plugin version is always 
                        encountered after its short name in <plugin> tag children
                        """
                        if TAGS["SHORT_NAME"] == element.tag:
                            plugin_line = element.text
                        elif TAGS["VERSION"] == element.tag:
                            plugins.append(plugin_line + ":" + element.text)
                            plugin_line = ""
                except ET.ParseError as parse_err:
                    print(
                        "Jenkins response is not in parsable XML format, "
                        "check your access rights to the instance: {parse_err}"
                        .format(parse_err=parse_err)
                    )
                    return 1
    for plugin in sorted(plugins):
        print(plugin)
    return 0


if "__main__" == __name__:
    sys.exit(main())
