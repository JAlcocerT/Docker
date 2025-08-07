#!/usr/bin/env node
/**
 * Create PocketBase collections programmatically using JavaScript
 * First install: npm install pocketbase dotenv
 */

require('dotenv').config();
const PocketBase = require('pocketbase');

// Initialize PocketBase client
const pb = new PocketBase('http://localhost:8080');

async function createCollections() {
    try {
        // Check if environment variables are loaded
        const adminEmail = process.env.PB_ADMIN_EMAIL;
        const adminPassword = process.env.PB_ADMIN_PASS;
        
        if (!adminEmail || !adminPassword) {
            console.error('❌ Missing credentials. Please check your .env file.');
            console.error('Required variables: PB_ADMIN_EMAIL, PB_ADMIN_PASS');
            return;
        }
        
        // Authenticate as admin
        console.log(`🔐 Authenticating as admin (${adminEmail})...`);
        await pb.admins.authWithPassword(adminEmail, adminPassword);
        console.log('✅ Authentication successful!');

        // Create a "products" collection
        const productsCollection = {
            name: 'products',
            type: 'base',
            schema: [
                {
                    name: 'name',
                    type: 'text',
                    required: true,
                    options: {
                        min: 1,
                        max: 100
                    }
                },
                {
                    name: 'description',
                    type: 'editor',
                    required: false
                },
                {
                    name: 'price',
                    type: 'number',
                    required: true,
                    options: {
                        min: 0
                    }
                },
                {
                    name: 'category',
                    type: 'select',
                    required: true,
                    options: {
                        maxSelect: 1,
                        values: ['electronics', 'clothing', 'books', 'home', 'sports']
                    }
                },
                {
                    name: 'images',
                    type: 'file',
                    required: false,
                    options: {
                        maxSelect: 5,
                        maxSize: 5242880, // 5MB
                        mimeTypes: ['image/jpeg', 'image/png', 'image/webp']
                    }
                },
                {
                    name: 'in_stock',
                    type: 'bool',
                    required: false,
                    options: {
                        default: true
                    }
                },
                {
                    name: 'sku',
                    type: 'text',
                    required: true,
                    options: {
                        min: 3,
                        max: 20,
                        pattern: '^[A-Z0-9-]+$'
                    }
                }
            ],
            listRule: '', // Public read
            viewRule: '', // Public read
            createRule: '@request.auth.id != ""', // Authenticated users only
            updateRule: '@request.auth.id != ""',
            deleteRule: '@request.auth.id != ""'
        };

        console.log('🛍️ Creating "products" collection...');
        const productsResult = await pb.collections.create(productsCollection);
        console.log(`✅ Collection "${productsResult.name}" created successfully!`);

        // Create a "reviews" collection with relation to products
        const reviewsCollection = {
            name: 'reviews',
            type: 'base',
            schema: [
                {
                    name: 'product',
                    type: 'relation',
                    required: true,
                    options: {
                        collectionId: productsResult.id,
                        cascadeDelete: true,
                        minSelect: 1,
                        maxSelect: 1
                    }
                },
                {
                    name: 'reviewer_name',
                    type: 'text',
                    required: true,
                    options: {
                        min: 1,
                        max: 100
                    }
                },
                {
                    name: 'rating',
                    type: 'number',
                    required: true,
                    options: {
                        min: 1,
                        max: 5
                    }
                },
                {
                    name: 'comment',
                    type: 'text',
                    required: false,
                    options: {
                        max: 1000
                    }
                },
                {
                    name: 'verified_purchase',
                    type: 'bool',
                    required: false,
                    options: {
                        default: false
                    }
                }
            ],
            listRule: '', // Public read
            viewRule: '', // Public read
            createRule: '@request.auth.id != ""',
            updateRule: '@request.auth.id != "" && reviewer_name = @request.auth.name',
            deleteRule: '@request.auth.id != "" && reviewer_name = @request.auth.name'
        };

        console.log('⭐ Creating "reviews" collection...');
        const reviewsResult = await pb.collections.create(reviewsCollection);
        console.log(`✅ Collection "${reviewsResult.name}" created successfully!`);

        console.log('\n🎉 All collections created successfully!');
        
        // List all collections to verify
        console.log('\n📋 Current collections:');
        const collections = await pb.collections.getFullList();
        collections.forEach(collection => {
            console.log(`  - ${collection.name} (${collection.type})`);
        });

    } catch (error) {
        console.error('❌ Error creating collections:', error);
    }
}

// Run the script
createCollections();
