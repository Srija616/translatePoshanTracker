url_main = "https://www.poshantracker.in"
raw_data_directory = "raw_data"
raw_data_new_directory = "raw_data_new"
unsupported_directory = "clean_unsupported"
default_num_processes = 2

languages = ['English', 'हिंदी', 'ગુજરાતી', 'મરાઠી', 'ಕನ್ನಡ', 'മലയാളം', 'தமிழ்', 'తెలుగు', 'বাংলা', 'অসমীয়া', 'ਪੰਜਾਬੀ', 'ଓଡ଼ିଆ', 'नेपाली', 'डोगरी', 'कोंकणी',
             'सिंधी', 'बोडो', 'मैथिली', 'মণিপুরী', 'संथाली', 'اردو', 'کٲشُر']
language_codes = ['en', 'hi', 'gu', 'mr', 'kn', 'ml', 'ta', 'te', 'bn', 'as', 'pa', 'or', 'ne', 'doi', 'kok', 'sd', 'brx', 'mai', 'mni' , 'sat', 'ur', 'ks']

eng_lang =['English', 'Hindi', 'Gujarati', 'Marathi', 'Kannada', 'Malayalam', 'Tamil', 'Telugu', 'Bengali', 'Assamese', 'Punjabi', 'Oriya', 'Nepali', 'Dogri', 'Konkani', 'Sindhi', 'Bodo', 'Maithili', 'Manipuri', 'Santhali', 'Urdu', 'Kashmiri']
eng_lang_dict = dict(zip(eng_lang, language_codes))

ft_lang_supported = ['as', 'bn', 'en', 'gu', 'mr', 'kn', 'ml', 'ta', 'te', 'pa', 'sd', 'mai', 'ur', 'ne', 'or', 'hi']
indicTrans_supported = ['as', 'bn', 'gu', 'hi', 'kn', 'ml', 'mr', 'or', 'pa', 'ta', 'te']
indic_languages_m2m100 =  ['hi', 'gu', 'mr', 'kn', 'ml', 'ta', 'bn', 'pa', 'or', 'ne', 'sd', 'ur']

common_supported_languages = ['bn', 'gu', 'hi', 'kn', 'ml', 'mr', 'or', 'pa', 'ta', 'te', 'en']
un_supported_trans = ['as', 'ne', 'doi', 'kok', 'sd', 'brx', 'mai', 'mni', 'sat', 'ur', 'ks']