"""
Define model function
"""
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout


def create_model(vocab_size, embedding_units, lstm_units, dense_units, dropout_rate):
    """
    Create text prediction model
    """
    model = Sequential([
        Embedding(vocab_size, embedding_units),
        Dropout(dropout_rate),
        LSTM(lstm_units),
        Dropout(dropout_rate),
        Dense(dense_units, activation='relu'),
        Dense(vocab_size, activation='softmax')
    ])
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy'])
    model.summary()
    return model