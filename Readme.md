# Streamlit on Docker

## Run Streamlit

### Run the main script

Run `docker-compose up` to run `src/main.py` in streamlit.

then open [localhost:8501/?name=main](http://localhost:8501/?name=main) in your browser. 

### Run a different script

`docker-compose run --service-ports streamlit streamlit run src/altair.py` and open [localhost:8501/?name=altair](http://localhost:8501/?name=altair) in your browser.

## Format

Run `docker-compose run streamlit black src/`
