import mne
import numpy as np
import matplotlib.pyplot as plt

# Load EEG data (replace 'sample_eeg.edf' with your EEG data file path)
# Supported formats include EDF, BrainVision, etc.
def load_eeg_data(file_path):
    raw_data = mne.io.read_raw_edf(file_path, preload=True)
    print("Data Loaded Successfully")
    return raw_data

# Preprocess the data: Bandpass filter to remove noise and retain specific frequency bands
def preprocess_data(raw_data, low_freq=1, high_freq=40):
    raw_data.filter(low_freq, high_freq, fir_design='firwin')
    print(f"Data filtered between {low_freq}Hz and {high_freq}Hz")
    return raw_data

# Extract power spectral density (PSD) for insights
def extract_psd(raw_data):
    psd, freqs = mne.time_frequency.psd_welch(raw_data, fmin=1, fmax=40, n_fft=1024)
    avg_psd = np.mean(psd, axis=0)
    print("Power Spectral Density extracted")
    return freqs, avg_psd

# Provide actionable insights (e.g., dominant frequency band)
def provide_insights(freqs, avg_psd):
    dominant_freq = freqs[np.argmax(avg_psd)]
    print(f"Dominant frequency: {dominant_freq}Hz")
    if dominant_freq < 8:
        print("Insights: Brain activity is likely in the Delta/Theta range. This might indicate sleep or relaxation.")
    elif 8 <= dominant_freq <= 13:
        print("Insights: Brain activity is in the Alpha range. This might indicate relaxation or meditation.")
    elif 13 < dominant_freq <= 30:
        print("Insights: Brain activity is in the Beta range. This might indicate active thinking or focus.")
    else:
        print("Insights: Brain activity is in the Gamma range. This might indicate high-level cognitive functioning.")
    return dominant_freq

# Visualize the PSD
def plot_psd(freqs, avg_psd):
    plt.figure(figsize=(10, 5))
    plt.plot(freqs, avg_psd, label="Power Spectral Density")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power")
    plt.title("EEG Power Spectral Density")
    plt.legend()
    plt.grid()
    plt.show()

# Main function to tie everything together
def main():
    file_path = 'sample_eeg.edf'  # Replace with your EEG file path
    raw_data = load_eeg_data(file_path)
    
    # Preprocessing
    raw_data = preprocess_data(raw_data)
    
    # PSD Analysis
    freqs, avg_psd = extract_psd(raw_data)
    
    # Insights
    provide_insights(freqs, avg_psd)
    
    # Visualization
    plot_psd(freqs, avg_psd)

if __name__ == "__main__":
    main()
