# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MyPlug2
                                 A QGIS plugin
 test
                             -------------------
        begin                : 2017-11-14
        copyright            : (C) 2017 by dfs
        email                : fsdf
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MyPlug2 class from file MyPlug2.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .myplug2 import MyPlug2
    return MyPlug2(iface)
