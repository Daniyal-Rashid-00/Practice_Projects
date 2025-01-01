import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    st.results.share()

    results = st.results.dict()
    print(f"Download Speed: {results['download'] / 1_000_000:.2f} Mbps")
    print(f"Upload Speed: {results['upload'] / 1_000_000:.2f} Mbps")
    print(f"Ping: {results['ping']} ms")

if __name__ == "__main__":
    test_internet_speed()