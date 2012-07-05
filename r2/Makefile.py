# The contents of this file are subject to the Common Public Attribution
# License Version 1.0. (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
# License Version 1.1, but Sections 14 and 15 have been added to cover use of
# software over a computer network and provide for limited attribution for the
# Original Developer. In addition, Exhibit A has been modified to be consistent
# with Exhibit B.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
#
# The Original Code is reddit.
#
# The Original Developer is the Initial Developer.  The Initial Developer of
# the Original Code is reddit Inc.
#
# All portions of the code written by reddit are Copyright (c) 2006-2012 reddit
# Inc. All Rights Reserved.
###############################################################################

from r2.lib.translation import I18N_PATH
from r2.lib.plugin import PluginLoader
from r2.lib import js

print 'I18NPATH := ' + I18N_PATH

plugins = list(PluginLoader.available_plugins())
print 'PLUGINS := ' + ' '.join(plugin.name for plugin in plugins)
for plugin in plugins:
    print 'PLUGIN_PATH_%s := %s' % (plugin.name, PluginLoader.plugin_path(plugin))

js.load_plugin_modules()
modules = dict((k, m) for k, m in js.module.iteritems() if m.should_compile)
print 'JS_MODULES := ' + ' '.join(modules.iterkeys())
outputs = []
for name, module in modules.iteritems():
    outputs.extend(module.outputs)
    print 'JS_MODULE_OUTPUTS_%s := %s' % (name, ' '.join(module.outputs))
    print 'JS_MODULE_DEPS_%s := %s' % (name, ' '.join(module.dependencies))

print 'JS_OUTPUTS := ' + ' '.join(outputs)