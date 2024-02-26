from initial_images import Images

class ImagesLoader(Images):            
    
    def load_products_images(self, products):
        base_path = 'initial_images/'
        base = [                                        
            {"id": 20, "path": 'par_pesas_4_kg_1.jpeg','is_main':True},
            {"id": 20, "path": 'par_pesas_4_kg_2.jpeg','is_main':False},
            {"id": 20, "path": 'par_pesas_4_kg_3.jpeg','is_main':False},
            {"id": 20, "path": 'par_pesas_4_kg_4.jpeg','is_main':False},        
            {"id": 19, "path": 'par_8kg_1.jpeg','is_main':True},
            {"id": 19, "path": 'par_8kg_2.jpeg','is_main':False},
            {"id": 19, "path": 'par_8kg_3.jpeg','is_main':False},
            {"id": 19, "path": 'par_8kg_4.jpeg','is_main':False},
            {"id": 18, "path": 'par_6kg_1.jpeg','is_main':True},
            {"id": 18, "path": 'par_6kg_2.jpeg','is_main':False},
            {"id": 18, "path": 'par_6kg_3.jpeg','is_main':False},
            {"id": 18, "path": 'par_6kg_4.jpeg','is_main':False},
            {"id": 17, "path": 'par_pesas_10_kg_Y_barra_22.jpeg','is_main':True},
            {"id": 17, "path": 'par_pesas_10_kg_Y_barra_22_1.jpeg','is_main':False},            
            {"id": 16, "path": 'par_pesas_10_kg_1.jpeg','is_main':True},
            {"id": 16, "path": 'par_pesas_10_kg_2.jpeg','is_main':False},
            {"id": 16, "path": 'par_pesas_10_kg_3.jpeg','is_main':False},
            {"id": 16, "path": 'par_pesas_10_kg.jpeg','is_main':False},
            {"id": 15, "path": 'barra_romana_semi_solida_1.jpeg','is_main':True},
            {"id": 15, "path": 'barra_romana_semi_solida_2.jpeg','is_main':False},
            {"id": 14, "path": 'barra_Z_semi_solida_1.jpeg','is_main':True},
            {"id": 14, "path": 'barra_Z_semi_solida_2.jpeg','is_main':False},
            {"id": 13, "path": 'barra_Z_acero.jpeg','is_main':True},
            {"id": 13, "path": 'barra_Z_acero_1.jpeg','is_main':False},
            {"id": 12, "path": 'barra_romana_acero.jpeg','is_main':True},
            {"id": 12, "path": 'barra_romana_acero_1.jpeg','is_main':False},        
            {"id": 11, "path": 'seguros_acero_1.jpeg','is_main':True},
            {"id": 11, "path": 'seguros_acero_2.jpeg','is_main':False},
            {"id": 11, "path": 'seguros_acero_3.jpeg','is_main':False},
            {"id": 10, "path": 'IMG_50kg_1_z_b_m_1.jpeg','is_main':True},
            {"id": 10, "path": 'IMG_50kg_1_z_b_m_2.jpeg','is_main':False},
            {"id": 10, "path": 'IMG_50kg_1_z_b_m_3.jpeg','is_main':False},
            {"id": 9, "path": 'IMG_42kg_1_z_b_m_1.jpeg','is_main':True},
            {"id": 9, "path": 'IMG_42kg_1_z_b_m.jpeg','is_main':False},            
            {"id": 8, "path": 'IMG_kit_42kg_acero_1.jpeg','is_main':True},
            {"id": 8, "path": 'IMG_kit_42kg_acero_2.jpeg','is_main':False},
            {"id": 8, "path": 'IMG_kit_42kg_acero_3.jpeg','is_main':False},            
            {"id": 7, "path": 'IMG_barras_1.jpeg','is_main':False},
            {"id": 7, "path": 'IMG_barras_2.jpeg','is_main':False},
            {"id": 7, "path": 'IMG_barras_3.jpeg','is_main':False},
            {"id": 7, "path": 'IMG_barras_4.jpeg','is_main':False},
            {"id": 7, "path": 'IMG_barras_5.jpeg','is_main':True},
            {"id": 6, "path": '10_kg_acero.jpeg','is_main':True},
            {"id": 6, "path": '10_kg_acero_1.jpeg','is_main':False},
            {"id": 6, "path": '10_kg_acero_2.jpeg','is_main':False},
            {"id": 5, "path": 'IMG_80kg_1.jpeg','is_main':True},
            {"id": 5, "path": 'IMG_80kg_2.jpeg','is_main':False},
            {"id": 5, "path": 'IMG_80kg_3.jpeg','is_main':False},
            {"id": 5, "path": 'IMG_80kg_4.jpeg','is_main':False},
            {"id": 4, "path": 'IMG_42kg_1.jpeg','is_main':True},
            {"id": 4, "path": 'IMG_42kg_2.jpeg','is_main':False},
            {"id": 1, "path": 'IMG_34kg_2.jpeg','is_main':False},
            {"id": 1, "path": 'IMG_34kg_1.jpeg','is_main':True},
            {"id": 3, "path": 'barras_parlelas.jpg','is_main':True},
            {"id": 3, "path": 'barras_parlelas_1.jpg','is_main':False},
            {"id": 3, "path": 'barras_parlelas_1.jpg','is_main':False}, 
                       
        ]        
        
        for product in products:
            for item in base:
                if product.id == item['id']:
                    image = f"{base_path}{item['path']}"                    
                    imageObject = self.save_image(image, item["path"], item["is_main"])                    
                    if imageObject is not None:
                        product.images.add(imageObject)
                        print(f'Agregando imagen a pruduct {product.id}')