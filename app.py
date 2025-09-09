import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from src.helper import (
    get_pdf_text,
    get_text_chunks,
    get_vector_store,
    initialize_hf_llm,
    build_history_aware_rag_chain,
)


def main():
    st.set_page_config("Information Retrieval")
    st.header("Information Retrieval System💁")
        
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "rag_chain" not in st.session_state:
        st.session_state.rag_chain = None

    with st.sidebar:
        pdfs = st.file_uploader("Upload PDFs", accept_multiple_files=True, type=["pdf"])
        if st.button("Process", disabled=not pdfs):
            text = get_pdf_text(pdfs)
            chunks = get_text_chunks(text)
            vs = get_vector_store(chunks)
            llm = initialize_hf_llm()
            st.session_state.rag_chain = build_history_aware_rag_chain(llm, vs)
            st.session_state.chat_history = []
            st.success("Ready")

    for m in st.session_state.chat_history:
        with st.chat_message("user" if isinstance(m, HumanMessage) else "assistant"):
            st.write(m.content)

    if st.session_state.rag_chain is None:
        st.info("Upload and process PDFs to start.")
    else:
        q = st.chat_input("Ask something")
        if q:
            st.session_state.chat_history.append(HumanMessage(content=q))
            with st.chat_message("assistant"):
                out = st.session_state.rag_chain.invoke({"input": q, "chat_history": st.session_state.chat_history})
                ans = out.get("answer", "")
                st.write(ans)
                st.session_state.chat_history.append(AIMessage(content=ans))
            


if __name__ == "__main__":
    main()