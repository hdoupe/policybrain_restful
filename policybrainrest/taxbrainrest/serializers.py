from rest_framework import serializers

from taxbrainrest.models import ModelInput, ModelResult

import taxcalc

class ModelInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelInput
        fields = ["input_specs", "specs", "errors_warnings"]

    def create(self, validated_data):
        input_specs = validated_data["input_specs"]
        specs = taxcalc.Calculator.read_json_param_objects(
            input_specs,
            None
        )
        errors_warnings = taxcalc.tbi.reform_warnings_errors(
            specs
        )

        model_input = ModelInput(
            input_specs=input_specs,
            specs=specs,
            errors_warnings=errors_warnings
        )
        model_input.save()
        return model_input


class ModelResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=ModelResult
        fields = ["static_results"]
