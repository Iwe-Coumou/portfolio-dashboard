from dataclasses import dataclass, field
import streamlit as st

@dataclass
class WorkingPortfolio:
    original_weights: dict[str, float]
    current_weights: dict[str, float] = field(default_factory=dict)
    removed_assets: list[str] = field(default_factory=list)
    added_assets: dict[str, float] = field(default_factory=dict)
    step: int = 1
    
def init_builder(original_weights: dict):
    if "working_portfolio" not in st.session_state:
        st.session_state.working_portfolio = WorkingPortfolio(
            original_weights=original_weights,
            current_weights=original_weights.copy()
        )
        
def get_builder() -> WorkingPortfolio:
    return st.session_state.working_portfolio

def reset_builder():
    del st.session_state.working_portfolio
    