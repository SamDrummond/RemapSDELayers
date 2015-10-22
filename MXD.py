import arcpy


class Document(object):

    def __init__(self, path="CURRENT"):

        self._path = path
        self._layers = []
        self._sde_layers = []
        self._mxd = arcpy.mapping.MapDocument(self._path)

    def retrieve_sde_layers(self):

        self._data_frames_from_mxd()
        self._all_data_frame_layers_to_list()
        self._all_sde_layers()

        return self._sde_layers

    def _data_frames_from_mxd(self):

        self.data_frames = arcpy.mapping.ListDataFrames(self._mxd)

    def _all_data_frame_layers_to_list(self):

        for data_frame in self.data_frames:
            layers = arcpy.mapping.ListLayers(self._mxd, "", data_frame)
            self._layers.extend(layers)

    def _all_sde_layers(self):

        for layer in self._layers:

            if layer.supports("WORKSPACEPATH") and (".sde" in layer.dataSource):
                self._sde_layers.append(layer)

    def save(self):
        self._mxd.save()

        if self._path == 'CURRENT':
            arcpy.RefreshTOC()


    def __exit__(self, exc_type, exc_val, exc_tb):
        del self._layers
        del self._sde_layers
        del self._mxd
