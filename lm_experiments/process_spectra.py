import pandas as pd
import os
import numpy as np
from tqdm.notebook import tqdm

if __name__ == "__main__":

    # Process raw data files into spectral dataframes

    long_table = pd.read_csv("../processed_data/DRIAMS_combined_long_table.csv")

    for dset in ["A", "B", "C", "D"]:

        print("Processing DRIAMS-{}".format(dset))

        current_samples = long_table.loc[long_table.dataset == dset].sample_id.unique()

#        current_samples = sorted(list(long_table["sample_id"].unique()))
        samples_spectra = []

        for i, sample_id in tqdm(enumerate(current_samples)):
            spectrum = pd.read_csv(
                f"../data/DRIAMS-{dset}/binned_6000/2018/{sample_id}.txt",
                sep=" ",
                index_col=0,
            )
            samples_spectra.append(spectrum.values.flatten())
        samples_spectra = np.vstack(samples_spectra)

        spectra_df = pd.DataFrame(data=samples_spectra, index=current_samples)

        spectra_df.to_csv(
            "../data/DRIAMS-{}/spectra_binned_6000_2018_reprocessed.csv".format(dset)
        )

        print("DRIAMS-{} processed!".format(dset))
