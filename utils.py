import numpy as np

def braille():
  return {
      'a' : np.array([[1, 0], [0, 0], [0, 0]], dtype=bool),
      'b' : np.array([[1, 0], [1, 0], [0, 0]], dtype=bool),
      'c' : np.array([[1, 1], [0, 0], [0, 0]], dtype=bool),
      'd' : np.array([[1, 1], [0, 1], [0, 0]], dtype=bool),
      'e' : np.array([[1, 0], [0, 1], [0, 0]], dtype=bool),
      'f' : np.array([[1, 1], [1, 0], [0, 0]], dtype=bool),
      'g' : np.array([[1, 1], [1, 1], [0, 0]], dtype=bool),
      'h' : np.array([[1, 0], [1, 1], [0, 0]], dtype=bool),
      'i' : np.array([[0, 1], [1, 0], [0, 0]], dtype=bool),
      'j' : np.array([[0, 1], [1, 1], [0, 0]], dtype=bool),
      'k' : np.array([[1, 0], [0, 0], [1, 0]], dtype=bool),
      'l' : np.array([[1, 0], [1, 0], [1, 0]], dtype=bool),
      'm' : np.array([[1, 1], [0, 0], [1, 0]], dtype=bool),
      'n' : np.array([[1, 1], [0, 1], [1, 0]], dtype=bool),
      'o' : np.array([[1, 0], [0, 1], [1, 0]], dtype=bool),
      'p' : np.array([[1, 1], [1, 0], [1, 0]], dtype=bool),
      'q' : np.array([[1, 1], [1, 1], [1, 0]], dtype=bool),
      'r' : np.array([[1, 0], [1, 1], [1, 0]], dtype=bool),
      's' : np.array([[0, 1], [1, 0], [1, 0]], dtype=bool),
      't' : np.array([[0, 1], [1, 1], [1, 0]], dtype=bool),
      'u' : np.array([[1, 0], [0, 0], [1, 1]], dtype=bool),
      'v' : np.array([[1, 0], [1, 0], [1, 1]], dtype=bool),
      'w' : np.array([[0, 1], [1, 1], [0, 1]], dtype=bool),
      'x' : np.array([[1, 1], [0, 0], [1, 1]], dtype=bool),
      'y' : np.array([[1, 1], [0, 1], [1, 1]], dtype=bool),
      'z' : np.array([[1, 0], [0, 1], [1, 1]], dtype=bool),
      
      '1' : [np.array([[0, 1], [0, 1], [1, 1]], dtype=bool), np.array([[1, 0], [0, 0], [0, 0]], dtype=bool)],
      '2' : [np.array([[0, 1], [0, 1], [1, 1]], dtype=bool), np.array([[1, 0], [1, 0], [0, 0]], dtype=bool)],
      '3' : [np.array([[0, 1], [0, 1], [1, 1]], dtype=bool), np.array([[1, 1], [0, 0], [0, 0]], dtype=bool)],
      '4' : [np.array([[0, 1], [0, 1], [1, 1]], dtype=bool), np.array([[1, 1], [1, 0], [0, 0]], dtype=bool)],
      '5' : [np.array([[0, 1], [0, 1], [1, 1]], dtype=bool), np.array([[1, 0], [0, 1], [0, 0]], dtype=bool)],
      '6' : [np.array([[0, 1], [0, 1], [1, 1]], dtype=bool), np.array([[1, 1], [1, 0], [0, 0]], dtype=bool)],
      '7' : [np.array([[0, 1], [0, 1], [1, 1]], dtype=bool), np.array([[1, 1], [1, 1], [0, 0]], dtype=bool)],
      '8' : [np.array([[0, 1], [0, 1], [1, 1]], dtype=bool), np.array([[1, 0], [1, 1], [0, 0]], dtype=bool)],
      '9' : [np.array([[0, 1], [0, 1], [1, 1]], dtype=bool), np.array([[0, 1], [1, 0], [0, 0]], dtype=bool)],
      '0' : [np.array([[0, 1], [0, 1], [1, 1]], dtype=bool), np.array([[0, 1], [1, 1], [0, 0]], dtype=bool)],
  }