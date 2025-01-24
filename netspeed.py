import speedtest
from com import speak

def speed_test():

    '''This function is used to check the network speed of the system'''

    try:
        wifi = speedtest.Speedtest()
    except speedtest.ConfigRetrievalError:
        speak("Failed to retrieve speedtest configuration. Please try again later.")
        return

    upload_net = round(wifi.upload()/1048576, 2)
    download_net = round(wifi.download()/1048576, 2)
    speak("Speedtest done successfully")
    print("Upload speed is: ", upload_net, "Mbps")
    speak(f"Upload speed is: {upload_net}% Mbps")
    print("Download speed is: ", download_net, "Mbps")
    speak(f"Download speed is: {download_net}% Mbps")

