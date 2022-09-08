# <div align="center">ESP Alarm Tags and Language Generator</div>

<div align="left">

<p>

This program is designed to create ESP Alarm Database [Tags](https://github.com/m-javed/ESPAlarmLanguage/blob/master/CSVExport/AlmTags.csv) and Language [Texts](https://github.com/m-javed/ESPAlarmLanguage/blob/master/CSVExport/AlmTexts.csv) files from TIA Portal ESAlarm DB copied to [excel file](https://github.com/m-javed/ESPAlarmLanguage/blob/master/Source/ESAlarms.xlsx).

</p>

</div>

## <div align="left">Translation</div>
Translation from English text to Chinese text is possible. Function <i>translate_to_chinese</i> from <i>functions.py</i> can be used for this purpose. A local copy of [available translations](https://github.com/m-javed/ESPAlarmLanguage/blob/master/available_translations.csv) is given priority when translating text. If no translation is found locally, an attempt is made to translate online with [Google Translate API](https://rapidapi.com/googlecloud/api/google-translate1/) or [Microsoft Translate API](https://rapidapi.com/microsoft-azure-org-microsoft-cognitive-services/api/microsoft-translator-text). Users can make adjustments accordingly. However you need to get your own API-Key, otherwise a message <i>"You are not subscribed to this API"</i> will be displayed. Because, with a free subscription of the above translation APIs a limited number of characters can be translated hence when a translation is found online it is appended to the local copy of available translations.

## <div align="center">Rights Disclaimer</div>

This program should not be used for commercial purposes and users of this program are requested to ahdere to the terms and conditions of the translation APIs used in this program.

<br>

## <div align="center">Contact</div>

For bugs and feature requests please visit [GitHub Issues](https://github.com/m-javed/ESPAlarmLanguage/issues).

<br>