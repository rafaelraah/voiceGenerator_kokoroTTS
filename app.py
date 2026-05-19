import streamlit as st
from kokoro import KPipeline 
import soundfile as sf
import numpy as np  
import tempfile

##Configurando a página no streamlit
st.set_page_config(
    page_title="Kokoro TTS",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 Kokoro Text To Speech")
st.markdown("Transforme texto em voz usando o modelo de IA Kokoro.")
st.markdown("Robusteça a sua experiência em geração de voz")

lang_code = "p"

##pipeline = kp(lang_code=lang_code)

##CARREGAR O MODELO:
@st.cache_resource
def load_pipeline():
    return KPipeline(
        repo_id="hexgrad/Kokoro-82M",
        lang_code="p"
    )

pipeline = load_pipeline()

texto = st.text_area(
    "Digite o texto",
    height=200,
    placeholder="Digite algo aqui..."
)

##Selecionar a voz
voice = st.selectbox(
    "Escolha a voz",
    [
        "af_heart",
        "af_bella",
        "af_nicole",
        "am_adam",
        "am_michael",
    ]
)

if st.button("Gerar Áudio"):

    if not texto.strip():
        st.warning("Digite algum texto.")
        st.stop()

    with st.spinner("Gerando áudio..."):

        generator = pipeline(
            texto,
            voice=voice
        )

        audio_chunks = []

        for gs, ps, audio in generator:
            audio_chunks.append(audio)

        final_audio = np.concatenate(audio_chunks)

        # salvar temporariamente
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as tmpfile:

            sf.write(
                tmpfile.name,
                final_audio,
                24000
            )

            audio_path = tmpfile.name

    st.success("Áudio gerado com sucesso!")

    # player
    st.audio(audio_path)

    # download
    with open(audio_path, "rb") as file:
        st.download_button(
            label="⬇️ Baixar Áudio",
            data=file,
            file_name="kokoro_audio.wav",
            mime="audio/wav"
        )


# for gs, ps, audio in generator:
#     audio_chunks.append(audio)

# audio_completo = np.concatenate(audio_chunks)
# sf.write("audio3.wav", audio_completo, 25000)