import uvicorn

def main():
    uvicorn.run(
        "src.app:app",
        host="localhost",
        port=8070,
        reload=True
    )

if __name__ == "__main__":
    main()
