import typing as t
from loguru import logger
from pathlib import Path
import torch
from transformers import PreTrainedModel
from transformers import PreTrainedTokenizer


class ModelLoader:
    """ModelLoader
    Downloading and Loading Hugging FaceModels
       Download occurs only when model is not located in the local model directory
       If model exists in local directory, load.

    """

    def __init__(
        self,
        model_name: str,
        model_directory: str,
        tokenizer_loader: PreTrainedTokenizer,
        model_loader: PreTrainedModel,
    ):

        self.model_name = Path(model_name)
        self.model_directory = Path(model_directory)
        self.model_loader = model_loader
        self.tokenizer_loader = tokenizer_loader

        self.save_path = self.model_directory / self.model_name

        if not self.save_path.exists():
            logger.debug(f"[+] {self.save_path} does not exit!")
            self.save_path.mkdir(parents=True, exist_ok=True)
            self.__download_model()

        self.tokenizer, self.model = self.__load_model()

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.save_path})"

    # Download model from HuggingFace
    def __download_model(self) -> None:

        logger.debug(f"[+] Downloading {self.model_name}")
        tokenizer = self.tokenizer_loader.from_pretrained(f"{self.model_name}")
        model = self.model_loader.from_pretrained(f"{self.model_name}")

        logger.debug(f"[+] Saving {self.model_name} to {self.save_path}")
        tokenizer.save_pretrained(f"{self.save_path}")
        model.save_pretrained(f"{self.save_path}")

        logger.debug("[+] Process completed")

    # Load model
    def __load_model(self) -> t.Tuple:

        logger.debug(f"[+] Loading model from {self.save_path}")
        tokenizer = self.tokenizer_loader.from_pretrained(f"{self.save_path}")
        # Check if GPU is available
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"[+] Model loaded in {device} complete")
        model = self.model_loader.from_pretrained(f"{self.save_path}").to(device)

        logger.debug("[+] Loading completed")
        return tokenizer, model

    def retrieve(self) -> t.Tuple:

        """Retriver

        Returns:
            Tuple: tokenizer, model
        """
        return self.tokenizer, self.model
