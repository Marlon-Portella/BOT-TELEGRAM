def sample_responses(input_text):
  user_massge = str(input_text).lower()

  if user_massge in("oi","ola","olá"):
    return "Aoba, bão?"
  elif "canal" in user_massge:
    return "ThePhax: https://youtube.com/@thephax7562?si=j2h0x4_ZbF9cYv7C \n     Inscreva-se"     

  return "não estou entendo você! tente novamente"