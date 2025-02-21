import numpy as np

from classification_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    expected_first_prediction_value = 0
    expected_no_predictions = 418

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    print('first row = ', sample_input_data.iloc[0])

    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.int64)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert predictions[0] == expected_first_prediction_value
