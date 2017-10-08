# Copyright 2012 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""
The Folder Project module handles creating Jenkins folder projects.

Example::

  job:
    name: test_folder
    project-type: folder
"""

import xml.etree.ElementTree as XML

import jenkins_jobs.modules.base

AVAILABLE_METRICS = {
    'worst-child-health-metric': 'com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric'
}


class Folder(jenkins_jobs.modules.base.Base):
    sequence = 0

    def root_xml(self, data):
        xml_parent = XML.Element('com.cloudbees.hudson.plugins.folder.Folder')
        XML.SubElement(xml_parent, 'icon',
                       attrib={'class': 'com.cloudbees.hudson.plugins.folder.icons.StockFolderIcon'})
        health_metrics = data.get('health-metrics', [])
        metrics = XML.SubElement(xml_parent, 'healthMetrics')
        for health_metric in health_metrics:
            if health_metric in AVAILABLE_METRICS.keys():
                XML.SubElement(metrics, AVAILABLE_METRICS.get(health_metric))
        return xml_parent
