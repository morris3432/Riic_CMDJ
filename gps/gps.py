from opencage.geocoder import OpenCageGeocode #libreria del gps

OCG = OpenCageGeocode("a3fe2b1f3ca644adad3d5c986d1910f5") #api keys
results = OCG.reverse_geocode(14.666, 76.833) #parametros de resultado
print(results[0],format) 

results = OCG.geocode(u'Guatemala')#ubicacion (iria la placa)
print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))

results = OCG.geocode(u'guatemala', language='de')
print(results[0]['components']['country'])#imprime resultado
