import streamlit as st
from api_02 import *
from textblob import TextBlob
from sentiment import *
from summarization import *
from recordmic import *
from audioplot import *

def process_audio_file(filename):
    audio_url = upload(filename)
    print(audio_url)
    # audioPlot(filename)

    st.write("Your File got processed successfully!")
    # st.write("Please choose an option below to view the results.")

    # save_transcript(audio_url, 'transcript')
    # with open('transcript.txt', 'r') as file:
    #     file_read = file.read().rstrip()

    # if st.button("View Transcript"):
    #     st.write("Transcript:")
    #     st.write(file_read)

    # if st.button("View Sentiment Analysis"):
    #     save_transcript(audio_url, 'transcript')
    #     with open('transcript.txt', 'r') as file:
    #         file_read = file.read().rstrip()
    #     analyze_text(file_read)

    # if st.button("View Summary"):
    #     save_transcript(audio_url, 'transcript')
    #     with open('transcript.txt', 'r') as file:
    #         file_read = file.read().rstrip()
    #     summarize_text(file_read)

    # fig = audioPlot(filename)

    # Display the plots using st.pyplot
    # st.pyplot(fig[0])
    # st.pyplot(fig[1])

    save_transcript(audio_url, 'transcript')

    with open('transcript.txt', 'r') as file:
        file_read = file.read().rstrip()

    with st.expander("Transcript:"):
        st.write(file_read)

    # print(file_read)

    # Doing sentimental analysis of text
    analyze_text(file_read)

    with open('sentiment_report.txt', 'r') as file:
        sentiment_report_file_read = ""
        # Loop through each line of the file
        for line in file:
            # Add the line to the file_contents variable
            sentiment_report_file_read += line + '\n'
        # sentiment_report_file_read = file.read()

    # st.write("sentiment report:")
    # st.write(sentiment_report_file_read)
    with st.expander("Sentiment Report:"):
        st.write(sentiment_report_file_read)

    with open('Statements.txt', 'r') as file:
        statements_file_read = file.read().rstrip()

    # st.write("Types of Statements made List:")
    # st.write(statements_file_read)
    with st.expander("Types of Statements made List:"):
        st.write(statements_file_read)

    # Doing summarization of text
    summarize_text(file_read)
    with open('summary.txt', 'r') as file:
        summary_file_read = file.read().rstrip()

    # st.write("Summary:")
    # st.write(summary_file_read)
    with st.expander("Summary:"):
        st.write(summary_file_read)

def main():
    st.title("Audio Processing App")
    st.write("This app allows you to upload a WAV file or record audio using your microphone.")
    st.write("Once the audio has been processed, it will perform sentiment analysis and summarization on the resulting transcript.")

    option = st.radio("Choose an option:", ("Upload WAV file", "Record Audio"))

    if option == "Upload WAV file":
        uploaded_file = st.file_uploader("Choose a WAV file", type="wav")
        if uploaded_file is not None:
            with open("uploaded.wav", "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("File uploaded successfully!")
            if st.button("Process File"):
                process_audio_file("uploaded.wav")

    elif option == "Record Audio":
        # duration = st.slider("Recording duration (seconds)", min_value=1, max_value=10, value=5, step=1)
        if st.button("Start Recording"):
            st.write("Recording...")
            with st.spinner('Recording in progress...'):
                filename = recordMic()
                st.success("Recording complete!")
                st.audio(open(filename, "rb").read(), format="audio/wav")
        # print(st.button("Process File"))
        if st.button("Process File"):
            try:
                process_audio_file("recorded_output.wav")
            except Exception as e:
                st.error("Error processing audio file:" + str(e))


if __name__ == "__main__":
    main()
