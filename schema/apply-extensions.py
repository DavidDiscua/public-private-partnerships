## ToDo: Replace requests JSON get with ordered dictionary
## Get process to make it's own backup and switch this back in at the end.

import requests
import json
import json_merge_patch
from collections import OrderedDict

extensions_to_merge = ['ppp','process_title','location','requirements','budget','budget_project','documentation_details','metrics','risk_allocation','shareholders','related_process','finance','milestones','qualification','tariffs','performance-failures','signatories','charges','transaction_milestones','bids','milestone_documents']

GIT_REF = "master"
location = "http://standard.open-contracting.org/extension_registry/{}/extensions.json".format(GIT_REF)
extension_json = requests.get(location).json()

with open('base-release-schema.json') as schema_file:
    schema = json.load(schema_file,object_pairs_hook=OrderedDict)

for extension in extension_json['extensions']:
    try:
        if extension['slug'] in extensions_to_merge:
            print("Merging " + extension['slug'] )
            extension_patch = requests.get(extension['url'].rstrip("/") + "/" + "release-schema.json").json()
            schema = json_merge_patch.merge(schema, extension_patch)


            extension_readme = requests.get(extension['url'].rstrip("/") + "/" + "README.md")
            with open('../docs/extensions/' + extension['slug'] + '.md','w') as readme:
                readme.write(extension_readme.text)

    except KeyError:
        print("Nothing")
        pass

with open("../release-schema.json") as local_patch:
    local_json = json.load(local_patch,object_pairs_hook=OrderedDict)
    schema = json_merge_patch.merge(schema, local_json)

with open('ppp-release-schema.json','w') as schema_file:
    json.dump(schema,schema_file,indent=4)

    