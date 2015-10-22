import MXD
import CSVFile
import Layer
import Logger

data_source_map_list = CSVFile.csv_to_list()
map_document = MXD.Document()

sde_layers = map_document.retrieve_sde_layers()
repath_candidates = Layer.repath_candidates_list_from_map_layers(sde_layers)

for candidate in repath_candidates:

    matches = [data_source_map for data_source_map in data_source_map_list
               if Layer.is_candidate_data_source_map(data_source_map, candidate)]

    if len(matches) == 1:

        match = matches[0]
        is_repath_success = candidate.repath(match)

        if is_repath_success:
            Logger.log_message("Resolved: " + matches[0][2] + "." + matches[0][3] + " to " +
                               matches[0][1] + " using " + matches[0][0])
        else:

            Logger.log_warning(matches[0][2] + "." + matches[0][3] + " could not be mapped to " +
                               matches[0][1] + " using " + matches[0][0])

    else:

        Logger.log_warning(candidate.feature_class_name + ": has " + str(len(matches)) +
                           " matches and has not been repathed.")

map_document.save()
