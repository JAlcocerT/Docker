version: '3.9'

services:
  chroma:
    container_name: chroma-container
    image: chromadb/chroma
    ports:
      - "8001:8000"
    volumes:
      - chroma_data:/chroma/chroma

volumes:
  chroma_data:
    driver: local
