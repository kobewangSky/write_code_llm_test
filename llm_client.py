"""
LLM call module - interact with local LLM through Ollama
"""
import logging
import time
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False
    logger.warning("Ollama not installed, please run: pip install ollama")

class LLMClient:
    def __init__(self, model: str = "gpt-oss:20b", timeout: int = 30, max_retries: int = 3):
        self.model = model
        self.timeout = timeout
        self.max_retries = max_retries
        
        if not OLLAMA_AVAILABLE:
            raise ImportError("Ollama module not installed")
        
        logger.info(f"Initializing LLM client: model={model}, timeout={timeout}s")
    
    def call_llm(self, prompt: str) -> Optional[str]:
        """Call LLM to generate response"""
        if not prompt.strip():
            logger.error("Prompt cannot be empty")
            return None
        
        for attempt in range(self.max_retries):
            try:
                logger.debug(f"Calling LLM (attempt {attempt + 1}/{self.max_retries})")
                start_time = time.time()
                
                response = ollama.chat(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    options={"timeout": self.timeout}
                )
                
                elapsed_time = time.time() - start_time
                
                if 'message' in response and 'content' in response['message']:
                    content = response['message']['content']
                    logger.info(f"LLM response successful (time: {elapsed_time:.2f}s, length: {len(content)} characters)")
                    return content
                else:
                    logger.error(f"LLM response format error: {response}")
                    
            except Exception as e:
                logger.error(f"LLM call failed (attempt {attempt + 1}/{self.max_retries}): {e}")
                
                if attempt < self.max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    logger.info(f"Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                else:
                    logger.error("All retries failed")
                    
        return None
    
    def call_llm_with_context(self, context_prompt: str) -> Optional[str]:
        """Call LLM with context (same as call_llm, but used to distinguish context calls)"""
        return self.call_llm(context_prompt)
    
    def test_connection(self) -> bool:
        """Test connection to Ollama"""
        try:
            logger.info("Testing LLM connection...")
            response = self.call_llm("Hello, please respond with 'OK' if you can hear me.")
            
            if response:
                logger.info("LLM connection test successful")
                return True
            else:
                logger.error("LLM connection test failed: no response")
                return False
                
        except Exception as e:
            logger.error(f"LLM connection test failed: {e}")
            return False
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get model information"""
        try:
            models = ollama.list()
            for model in models.get('models', []):
                if model.get('name') == self.model:
                    return model
            return {}
        except Exception as e:
            logger.error(f"Failed to get model information: {e}")
            return {}