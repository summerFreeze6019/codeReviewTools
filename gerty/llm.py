import os, sys
from typing import Optional, List, Dict, Any
from langchain.llms import LlamaCpp
from langchain import LLMChain
from langchain.callbacks.manager import CallbackManager

class LlamaCppMiroStat(LlamaCpp): 
    """
    This class only exists to allow me to be able to
    explicitly set the mirostat mode, eta, and tau values for generation.
    """

    def _get_parameters(self, stop: Optional[List[str]] = None) -> Dict[str, Any]:
        if self.stop and stop is not None:
            raise ValueError("`stop` found in both the input and default params.")

        params = self._default_params

        # llama_cpp expects the "stop" key not this, so we remove it:
        params.pop("stop_sequences")

        # then sets it as configured, or default to an empty list:
        params["stop"] = self.stop or stop or []


        params["mirostat_mode"] = 2
        params["mirostat_eta"] = 0.1
        params["mirostat_tau"] = 5.0

        return params



def get_model(
    model_path: str = os.path.realpath(
        os.path.join(os.path.dirname(__file__), "models", "nous-hermes-llama-2-7b")
    ),
    n_ctx=2048,
    n_gpu_layers = 25,
    n_batch = 512,
    callback_manager: Optional[CallbackManager] = None,
):
    """
    A simple helper to retrieve the llama model in question.
    """
    num_cores: int = os.cpu_count() or 1

    llm = LlamaCppMiroStat(
        model_path=os.path.join( model_path, "ggml-model-q4_k.bin" ),
        n_gpu_layers=n_gpu_layers,
        n_batch=n_batch,
        callback_manager=callback_manager,
        stop=["\n###", "Human:"],  # ["Human:", "\n\n"],
        n_ctx=n_ctx,
        f16_kv=True,
        verbose=False,
        n_threads = num_cores//2,
    )
    llm.client.verbose = False
    return llm


