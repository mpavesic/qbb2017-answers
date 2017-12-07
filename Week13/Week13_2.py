#!/usr/bin/env python

$ grep ">" bins/bin.1.fa | head -5

>NODE_14_length_235766_cov_39.967778
>NODE_25_length_133218_cov_37.848772
>NODE_40_length_102363_cov_33.084783
>NODE_49_length_91030_cov_33.607782
>NODE_56_length_87142_cov_32.060330

$ grep NODE_14_length_235766_cov_39.967778 week13_data/KRAKEN/assembly.kraken 
NODE_14_length_235766_cov_39.967778	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus;Staphylococcus haemolyticus JCSC1435
$ grep NODE_25_length_133218_cov_37.848772 week13_data/KRAKEN/assembly.kraken 
NODE_25_length_133218_cov_37.848772	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus;Staphylococcus haemolyticus JCSC1435
$ grep NODE_40_length_102363_cov_33.084783 week13_data/KRAKEN/assembly.kraken 
NODE_40_length_102363_cov_33.084783	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus;Staphylococcus haemolyticus JCSC1435
$ grep NODE_49_length_91030_cov_33.607782 week13_data/KRAKEN/assembly.kraken 
NODE_49_length_91030_cov_33.607782	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus;Staphylococcus haemolyticus JCSC1435
$ grep NODE_56_length_87142_cov_32.060330 week13_data/KRAKEN/assembly.kraken 
NODE_56_length_87142_cov_32.060330	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus;Staphylococcus haemolyticus JCSC1435

Bin 1 = root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus;Staphylococcus haemolyticus JCSC1435

$ grep ">" bins/bin.2.fa | head -5

>NODE_30_length_116726_cov_3.835555
>NODE_66_length_80937_cov_3.162644
>NODE_184_length_42741_cov_3.497774
>NODE_188_length_41458_cov_2.793107
>NODE_213_length_37420_cov_6.653820

$ grep NODE_30_length_116726_cov_3.835555 week13_data/KRAKEN/assembly.kraken 
NODE_30_length_116726_cov_3.835555	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Leuconostocaceae;Leuconostoc;Leuconostoc citreum;Leuconostoc citreum KM20
$ grep NODE_66_length_80937_cov_3.162644 week13_data/KRAKEN/assembly.kraken
NODE_66_length_80937_cov_3.162644	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Leuconostocaceae;Leuconostoc;Leuconostoc citreum;Leuconostoc citreum KM20
$ grep NODE_184_length_42741_cov_3.497774 week13_data/KRAKEN/assembly.kraken
NODE_184_length_42741_cov_3.497774	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Leuconostocaceae;Leuconostoc;Leuconostoc citreum;Leuconostoc citreum KM20
$ grep ODE_188_length_41458_cov_2.793107 week13_data/KRAKEN/assembly.kraken 
NODE_188_length_41458_cov_2.793107	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Leuconostocaceae;Leuconostoc;Leuconostoc citreum;Leuconostoc citreum KM20
$ grep NODE_213_length_37420_cov_6.653820 week13_data/KRAKEN/assembly.kraken
NODE_213_length_37420_cov_6.653820	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Leuconostocaceae;Leuconostoc;Leuconostoc citreum;Leuconostoc citreum KM20 

Bin 2 = root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Leuconostocaceae;Leuconostoc;Leuconostoc citreum;Leuconostoc citreum KM20

$ grep ">" bins/bin.3.fa | head -5

>NODE_24_length_157060_cov_6.639394
>NODE_51_length_90307_cov_7.345411
>NODE_57_length_86315_cov_6.829585
>NODE_63_length_81315_cov_8.021302
>NODE_64_length_81158_cov_8.284465

$ grep NODE_24_length_157060_cov_6.639394 week13_data/KRAKEN/assembly.kraken 
NODE_24_length_157060_cov_6.639394	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus lugdunensis;Staphylococcus lugdunensis HKU09-01
$ grep NODE_51_length_90307_cov_7.345411 week13_data/KRAKEN/assembly.kraken 
NODE_51_length_90307_cov_7.345411	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus lugdunensis;Staphylococcus lugdunensis HKU09-01
$ grep NODE_57_length_86315_cov_6.829585 week13_data/KRAKEN/assembly.kraken 
NODE_57_length_86315_cov_6.829585	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus lugdunensis;Staphylococcus lugdunensis HKU09-01
$ grep NODE_63_length_81315_cov_8.021302 week13_data/KRAKEN/assembly.kraken 
NODE_63_length_81315_cov_8.021302	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus lugdunensis;Staphylococcus lugdunensis HKU09-01
$ grep NODE_64_length_81158_cov_8.284465 week13_data/KRAKEN/assembly.kraken 
NODE_64_length_81158_cov_8.284465	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus lugdunensis;Staphylococcus lugdunensis N920143

Bin 3 = root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus lugdunensis;Staphylococcus lugdunensis ... probably HKU09-01

$ grep ">" bins/bin.4.fa | head -5

>NODE_1_length_1447137_cov_2268.097092
>NODE_2_length_556123_cov_2361.439230
>NODE_8_length_298793_cov_2547.011572
>NODE_10_length_279092_cov_2597.445937
>NODE_16_length_219929_cov_2350.909321

$ grep NODE_1_length_1447137_cov_2268.097092 week13_data/KRAKEN/assembly.kraken
NODE_1_length_1447137_cov_2268.097092	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis OG1RF 
$ grep NODE_2_length_556123_cov_2361.439230 week13_data/KRAKEN/assembly.kraken 
NODE_2_length_556123_cov_2361.439230	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis V583
$ grep NODE_8_length_298793_cov_2547.011572 week13_data/KRAKEN/assembly.kraken
NODE_8_length_298793_cov_2547.011572	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis str. Symbioflor 1 
$ grep NODE_10_length_279092_cov_2597.445937 week13_data/KRAKEN/assembly.kraken
NODE_10_length_279092_cov_2597.445937	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis D32 
$ grep NODE_16_length_219929_cov_2350.909321 week13_data/KRAKEN/assembly.kraken 
NODE_16_length_219929_cov_2350.909321	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis V583

Bin 4 = NODE_1_length_1447137_cov_2268.097092	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis

$ grep ">" bins/bin.5.fa | head -5

>NODE_4_length_455101_cov_112.371015
>NODE_6_length_320041_cov_123.475336
>NODE_7_length_310076_cov_130.336474
>NODE_9_length_293536_cov_118.600107
>NODE_11_length_278925_cov_118.155370

$ grep NODE_4_length_455101_cov_112.371015 week13_data/KRAKEN/assembly.kraken
NODE_4_length_455101_cov_112.371015	root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067
$ grep NODE_6_length_320041_cov_123.475336 week13_data/KRAKEN/assembly.kraken
NODE_6_length_320041_cov_123.475336	root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067
$ grep NODE_7_length_310076_cov_130.336474 week13_data/KRAKEN/assembly.kraken
NODE_7_length_310076_cov_130.336474	root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067
$ grep NODE_9_length_293536_cov_118.600107 week13_data/KRAKEN/assembly.kraken
NODE_9_length_293536_cov_118.600107	root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067
$ grep NODE_11_length_278925_cov_118.155370 week13_data/KRAKEN/assembly.kraken
NODE_11_length_278925_cov_118.155370	root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067

Bin 5 = root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067

$ grep ">" bins/bin.6.fa | head -5

>NODE_20_length_181746_cov_381.691663
>NODE_29_length_119200_cov_370.287381
>NODE_41_length_101957_cov_389.183480
>NODE_61_length_82298_cov_454.296293
>NODE_67_length_80393_cov_402.833130

$ grep NODE_20_length_181746_cov_381.691663 week13_data/KRAKEN/assembly.kraken
NODE_20_length_181746_cov_381.691663	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis RP62A
$ grep NODE_29_length_119200_cov_370.287381 week13_data/KRAKEN/assembly.kraken
NODE_29_length_119200_cov_370.287381	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis ATCC 12228
$ grep NODE_41_length_101957_cov_389.183480 week13_data/KRAKEN/assembly.kraken
NODE_41_length_101957_cov_389.183480	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis ATCC 12228
$ grep NODE_61_length_82298_cov_454.296293 week13_data/KRAKEN/assembly.kraken
NODE_61_length_82298_cov_454.296293	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis RP62A
$ grep NODE_67_length_80393_cov_402.833130 week13_data/KRAKEN/assembly.kraken
NODE_67_length_80393_cov_402.833130	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis RP62A

Bin 6 = root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis

$ grep ">" bins/bin.7.fa | head -5

>NODE_12_length_269228_cov_106.168966
>NODE_21_length_175135_cov_99.919448
>NODE_22_length_170455_cov_103.210716
>NODE_23_length_162494_cov_110.139985
>NODE_26_length_127947_cov_99.828324

$ grep NODE_12_length_269228_cov_106.168966 week13_data/KRAKEN/assembly.kraken
NODE_12_length_269228_cov_106.168966	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1
$ grep NODE_21_length_175135_cov_99.919448 week13_data/KRAKEN/assembly.kraken
NODE_21_length_175135_cov_99.919448	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1
$ grep NODE_22_length_170455_cov_103.210716 week13_data/KRAKEN/assembly.kraken
NODE_22_length_170455_cov_103.210716	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1
$ grep NODE_23_length_162494_cov_110.139985 week13_data/KRAKEN/assembly.kraken
NODE_23_length_162494_cov_110.139985	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1
$ grep NODE_26_length_127947_cov_99.828324 week13_data/KRAKEN/assembly.kraken
NODE_26_length_127947_cov_99.828324	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1

Bin 7 = root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1

$ grep ">" bins/bin.8.fa | head -5

>NODE_3_length_498518_cov_181.760000
>NODE_5_length_427301_cov_143.861656
>NODE_15_length_235270_cov_153.562668
>NODE_19_length_199764_cov_200.017410
>NODE_31_length_114355_cov_167.687393

$ grep NODE_3_length_498518_cov_181.760000 week13_data/KRAKEN/assembly.kraken
NODE_3_length_498518_cov_181.760000	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Anaerococcus;Anaerococcus prevotii;Anaerococcus prevotii DSM 20548
$ grep NODE_5_length_427301_cov_143.861656 week13_data/KRAKEN/assembly.kraken
NODE_5_length_427301_cov_143.861656	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Anaerococcus;Anaerococcus prevotii;Anaerococcus prevotii DSM 20548
$ grep NODE_15_length_235270_cov_153.562668 week13_data/KRAKEN/assembly.kraken
NODE_15_length_235270_cov_153.562668	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Finegoldia;Finegoldia magna;Finegoldia magna ATCC 29328
$ grep NODE_19_length_199764_cov_200.017410 week13_data/KRAKEN/assembly.kraken
NODE_19_length_199764_cov_200.017410	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Anaerococcus;Anaerococcus prevotii;Anaerococcus prevotii DSM 20548
$ grep NODE_31_length_114355_cov_167.687393 week13_data/KRAKEN/assembly.kraken
NODE_31_length_114355_cov_167.687393	root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Streptococcaceae;Streptococcus;Streptococcus anginosus group;Streptococcus anginosus;Streptococcus anginosus C238

Bin 8 = root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes



