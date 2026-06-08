name: Build Flet APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

env:
  # GitHub so'rayotgan yangi Node.js 24 muhitini majburiy yoqamiz
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Set up Java (JDK 17)
        uses: actions/setup-java@v4
        with:
          distribution: 'zulu'
          java-version: '17'

      - name: Setup Flutter
        uses: subosito/flutter-action@v2
        with:
          channel: 'stable'

      - name: Install Flet CLI
        run: |
          pip install flet-cli

      - name: Build APK
        run: |
          flet build apk
          
      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: flet-app-apk
          path: build/apk/*.apk
