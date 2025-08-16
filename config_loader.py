"""
JSON configuration loading module
Load test configuration files containing prompts and questions
"""
import json
import logging
from typing import Dict, List, Any
from pathlib import Path

logger = logging.getLogger(__name__)

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.config = {}
        
    def load_config(self) -> Dict[str, Any]:
        """Load test configuration file"""
        try:
            if not self.config_path.exists():
                raise FileNotFoundError(f"Configuration file does not exist: {self.config_path}")
                
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
                
            logger.info(f"Successfully loaded configuration file: {self.config_path}")
            return self.config
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON format error: {e}")
            raise
        except Exception as e:
            logger.error(f"Failed to load configuration file: {e}")
            raise
    
    def get_prompts(self) -> Dict[str, str]:
        """Get all prompt templates"""
        prompts = {}
        for key, value in self.config.items():
            if (key.startswith('prompt') and 
                not key.endswith('_status') and 
                not key.endswith('_success') and 
                not key.endswith('_fail') and 
                isinstance(value, str)):
                prompts[key] = value
        
        if not prompts:
            logger.warning("No prompt templates found")
            
        return prompts
    
    def get_prompt_status(self, prompt_name: str) -> str:
        """Get dynamic status for a specific prompt (deprecated - use get_prompt_status_by_result)"""
        status_key = f"{prompt_name}_status"
        return self.config.get(status_key, "")
    
    def get_prompt_status_by_result(self, prompt_name: str, success: bool) -> str:
        """Get dynamic status based on result (success/fail)"""
        if success:
            status_key = f"{prompt_name}_success"
        else:
            status_key = f"{prompt_name}_fail"
        
        return self.config.get(status_key, "")
    
    def get_questions(self) -> List[Dict[str, str]]:
        """Get all test questions"""
        questions = self.config.get('questions', [])
        
        if not questions:
            logger.warning("No test questions found")
            
        # Validate question format
        for i, question in enumerate(questions):
            if 'question' not in question or 'answer' not in question:
                raise ValueError(f"Question {i+1} format error: missing 'question' or 'answer' field")
        
        return questions
    
    def validate_config(self) -> bool:
        """Validate configuration file format"""
        try:
            prompts = self.get_prompts()
            questions = self.get_questions()
            
            if not prompts:
                logger.error("No prompt templates in configuration file")
                return False
                
            if not questions:
                logger.error("No test questions in configuration file")
                return False
            
            # Check if prompt contains {question} placeholder
            for prompt_name, prompt_template in prompts.items():
                if '{question}' not in prompt_template:
                    logger.warning(f"Prompt '{prompt_name}' does not contain '{{question}}' placeholder")
            
            logger.info(f"Configuration file validation passed: {len(prompts)} prompts, {len(questions)} questions")
            return True
            
        except Exception as e:
            logger.error(f"Configuration file validation failed: {e}")
            return False