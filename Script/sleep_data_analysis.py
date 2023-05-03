import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne

# Load the sleep dataset
file_path = 'SC4001E0-PSG.edf' 
raw = mne.io.read_raw_edf(file_path, preload=True)

# Extract EEG, EOG, and EMG channels
eeg_channel = 'EEG Fpz-Cz'
eog_channel = 'EOG horizontal'
emg_channel = 'EMG submental'
raw.pick_channels([eeg_channel, eog_channel, emg_channel])

# Filter the data with a bandpass filter ranging from 0.5 Hz to 49 Hz
raw.filter(l_freq=0.5, h_freq=49)

# Plot a 30-second epoch of the sleep data
start_time = 1000  # in seconds
epoch_duration = 30  # in seconds
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15, 10), sharex=True)

# Loop over EEG, EOG, and EMG channels and plot their signals
for ax, channel in zip(axes, [eeg_channel, eog_channel, emg_channel]):
    # Extract data and time from the selected epoch
    data, times = raw[channel, int(start_time * raw.info['sfreq']):int((start_time + epoch_duration) * raw.info['sfreq'])]
    
    # Plot the data
    ax.plot(times, data.T)
    ax.set_title(channel)
    ax.set_ylabel('Amplitude (µV)')

# Set the label for the x-axis
axes[-1].set_xlabel('Time (s)')

# Save the figure as a PNG file with a resolution of 500 dpi and a tight bounding box
fig.savefig('sleep_data.png', dpi=500, bbox_inches='tight')

