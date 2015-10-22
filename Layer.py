import arcpy


def repath_candidates_list_from_map_layers(sde_layers):

    candidates = []

    for layer in sde_layers:
        candidate = Candidate(layer)

        if candidate.is_referenced_to_legacy_sde:
            candidates.append(candidate)

    return candidates


def is_candidate_data_source_map(data_source_map, candidate):

    return candidate.database == data_source_map[2] and candidate.feature_class_name == data_source_map[3]


class Candidate(object):

    def __init__(self, layer):

        self._layer = layer

        data_set_property_list = layer.datasetName.split(".")
        self._feature_class = data_set_property_list[len(data_set_property_list) - 1]

        workspace = arcpy.Describe(layer.workspacePath)
        connection_properties = workspace.connectionProperties

        self._server = connection_properties.server.split(".")[0]
        self._database = connection_properties.database

    @property
    def is_referenced_to_legacy_sde(self):
        return self._server == 'wmkarcgis'

    @property
    def feature_class_name(self):
        return self._feature_class

    @property
    def server(self):
        return self._server

    @property
    def database(self):
        return self._database

    @property
    def layer(self):
        return self._layer

    def repath(self, match):

        arcpy.env.workspace = match[0]
        match_exists = arcpy.Exists(match[1])

        print(arcpy.env.workspace + "\\" + match[1])

        if match_exists:
            self._layer.replaceDataSource(arcpy.env.workspace, "SDE_WORKSPACE", match[1])

        return match_exists
