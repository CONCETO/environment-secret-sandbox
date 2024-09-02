#!/bin/bash 

# Define paths
ENV_FILE="deployment-configs/pro/scheugrp/ci.tenant.env"
TEMPLATE_FILE="deployment-configs/shared/tenant.config.template.yaml"
OUTPUT_FILE="interpolated.yaml"

# Get all variable names, excluding comments and empty lines
VARS=$(grep -v '^#' "$ENV_FILE" | sed '/^\s*$/d' | cut -d'=' -f1)

# Read the template file content
TEMPLATE_CONTENT=$(cat "$TEMPLATE_FILE")

rm -Rf $OUTPUT_FILE

npx dotenv -e $ENV_FILE -- envsubst '$DATABASE_URL,$SUBACCOUNTID' < $TEMPLATE_FILE > $OUTPUT_FILE
# Iterate over each variable
# for VAR in $VARS; do
#     # npx dotenv -e $ENV_FILE -- envsubst '$SUBACCOUNTID' < $TEMPLATE_FILE > $OUTPUT_FILE
#     npx dotenv -e $ENV_FILE -- envsubst "$$(echo $VAR)" < $TEMPLATE_FILE > $OUTPUT_FILE
#     # Perform envsubst for the current variable
#     # INTERPOLATED=$(npx dotenv -e $ENV_FILE -- echo "$TEMPLATE_CONTENT" | VAR_NAME="$VAR" envsubst '$${!VAR_NAME}')
    
#     # Append the result to the output file
#     echo "Interpolation for $VAR"
#     echo "$INTERPOLATED" >> "$OUTPUT_FILE"
#     echo "" >> "$OUTPUT_FILE"  # Add a blank line for readability
# done

echo "Interpolation complete. Results written to $OUTPUT_FILE"