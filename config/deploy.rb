# config valid only for Capistrano 3.1
lock '3.2.1'

set :pty, true
set :scm, :git
set :keep_releases, 5
set :application, "stock_research"
set :repo_url, "git@github.com:hongo35/#{fetch(:application)}.git"
ask(:branch, "develop")

set :deploy_to, "/home/hongo35/#{fetch(:application)}"

set :linked_files, %w{stock_research/settings.py}

namespace :deploy do

  desc 'Restart application'
  task :restart do
    on roles(:app), in: :sequence, wait: 5 do
      # Your restart mechanism here, for example:
      # execute :touch, release_path.join('tmp/restart.txt')
    end
  end

  desc 'Upload config files'
  task :upload do
    on roles(:app) do |host|
      if test "[ ! -d #{shared_path}/stock_research ]"
        execute "mkdir -p #{shared_path}/stock_research"
      end
      upload!('stock_research/settings.py', "#{shared_path}/stock_research/settings.py")
    end
  end

  after :publishing, :restart

  after :restart, :clear_cache do
    on roles(:web), in: :groups, limit: 3, wait: 10 do
      # Here we can do anything such as:
      # within release_path do
      #   execute :rake, 'cache:clear'
      # end
    end
  end

end
