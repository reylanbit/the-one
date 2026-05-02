import numpy as np
import pygame

def generate_beep(frequency: int, duration: float, volume: float = 0.1) -> pygame.mixer.Sound:
    """Gera um som de bip simples usando numpy."""
    sample_rate = 44100
    n_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, n_samples, False)
    # Onda senoidal
    wave = np.sin(2 * np.pi * frequency * t) * volume
    # Converter para 16-bit PCM
    audio = (wave * 32767).astype(np.int16)
    # Tornar estéreo
    stereo_audio = np.column_stack((audio, audio))
    return pygame.sndarray.make_sound(stereo_audio)

class SoundManager:
    """Gerencia efeitos sonoros do SortViz."""

    def __init__(self):
        pygame.mixer.init()
        self.enabled = True
        try:
            self.sound_compare = generate_beep(440, 0.05) # A4
            self.sound_swap = generate_beep(880, 0.05)    # A5
        except Exception:
            self.enabled = False

    def play_compare(self):
        if self.enabled:
            self.sound_compare.play()

    def play_swap(self):
        if self.enabled:
            self.sound_swap.play()
